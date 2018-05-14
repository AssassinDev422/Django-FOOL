from __future__ import unicode_literals
from celery import shared_task
from logging import getLogger
import requests
import xmltodict
from django.conf import settings
from .models import CreditCard, CardIssuer

from .utils import (
    get_capital_one_access_token, get_capital_one_latest_card_details,
    get_capital_one_cards
)

logger = getLogger(__name__)

def parse_bullets_into_list(markup):
    bullet_characters = ['&#8226;', '&bull;']
    for bullet in bullet_characters:
        if bullet in markup:
            items = markup.split(bullet)
            items = filter(None, items)
            list_items = ['<li>{0}</li>'.format(item) for item in items]
            return '<ul>\n\t{0}\n\t</ul>'.format('\n'.join(list_items))
    return markup


def get_processing_network(text):
    if not text:
        return None
    for option in CreditCard.PROCESSING_NETWORKS:
        if CreditCard.PROCESSING_NETWORKS[option[0]].lower() in text.lower():
            return option[0]


@shared_task
def load_cj_feed():
    def get_value(fields, key):
        value = fields.get(key)
        if not value or 'null' in value or 'N/A' in value:
            return ''
        return value

    def get_transfer_apr_additional_language(card_description):
        if not card_description:
            return ''
        if 'introTransferAPR NOTE: For sites with space restrictions use: 0% Introductory (or Intro) APR' in card_description and 'qualifying balance transfers' in card_description:
            return 'for qualifying balance transfers'
        return ''


    def get_apr_value(apr_value, apr_period_value, apr_period_type, apr_extra_description=''):
        if apr_value:
            return "{0}%, {1} {2} {3}".format(apr_value, apr_period_value, apr_period_type, apr_extra_description).strip()
        else:
            return 'N/A'

    headers = {'authorization': settings.CJ_API_DEV_KEY}
    params = {
        'website-id': settings.CJ_API_WEBSITE_ID,
        'advertiser-ids': u','.join(map(unicode, CardIssuer.objects.filter(cj_advertiser_id__isnull=False).values_list('cj_advertiser_id', flat=True))),
        'link-type': 'Content Link',
        'records-per-page': 100
    }
    response = requests.get(settings.CJ_API_URI, headers=headers, params=params)

    try:
        response.raise_for_status()
    except:
        logger.exception('Error fetching credit card data from CJ feed')
        return

    feed = xmltodict.parse(response.text)

    for link in feed['cj-api']['links']['link']:
        try:
            fields = link['parsed-custom-content-fields']
        except KeyError:
            # most of the other logic here is based on this fields declaration, to not good to set other fields as empty if we can't get the fields initially
            continue
        description = link['description']

        name, slug = CreditCard.get_name_and_slug(get_value(fields, 'cardName'))
        marketing_copy = parse_bullets_into_list(get_value(fields, 'marketingCopy'))

        intro_purchase_apr_value = get_value(fields, 'introPurchAPRValue')
        intro_purchase_apr_type = get_value(fields, 'introPurchAPRValue')
        intro_purchase_apr_period = get_value(fields, 'introPurchAPRPeriod')
        intro_purchase_apr_period_value = get_value(fields, 'introPurchAPRPeriodValue')
        intro_purchase_apr_period_type = get_value(fields, 'introPurchAPRPeriodType')
        intro_purchase_apr = get_apr_value(intro_purchase_apr_value, intro_purchase_apr_period_value, intro_purchase_apr_period_type)
        purchase_apr = get_value(fields, 'nonIntroPurchAPR')
        intro_transfer_apr_value = get_value(fields, 'introTransferAPRValue')
        intro_transfer_apr_period_value = get_value(fields, 'introTransAPRPeriodValue')
        intro_transfer_apr_period_type = get_value(fields, 'introTransAPRPeriodType')
        intro_transfer_apr_extra_description = get_transfer_apr_additional_language(description)
        intro_transfer_apr = get_apr_value(intro_transfer_apr_value, intro_transfer_apr_period_value, intro_transfer_apr_period_type, intro_transfer_apr_extra_description)
        transfer_apr = get_value(fields, 'nonIntroTransAPR')
        credit_rating = get_value(fields, 'creditRating')
        annual_fee = get_value(fields, 'annualMemFee')
        image_source_url = link['images']['image']['url'] if link.get('images') else ''
        application_link = link.get('clickUrl', '')
        rewards_bonus = get_value(fields, 'rewardsBonus')
        rewards_bonus_terms = get_value(fields, 'rewardsBonusTerms')
        detailed_rates_and_fees_link = get_value(fields, 'detailsRatesFeesUrl')
        processing_network = get_processing_network(get_value(fields, 'processingNetwork'))
        issuer = CardIssuer.objects.get(cj_advertiser_id=link['advertiser-id'])
        defaults = {
            'slug': slug,
            'name': name,
            'marketing_copy': marketing_copy,
            'intro_purchase_apr': intro_purchase_apr,
            'purchase_apr': purchase_apr,
            'intro_transfer_apr': intro_transfer_apr,
            'transfer_apr': transfer_apr,
            'credit_rating': credit_rating,
            'annual_fee': annual_fee,
            'application_link': application_link,
            'rewards_bonus': rewards_bonus,
            'rewards_bonus_terms': rewards_bonus_terms,
            'issuer': issuer,
            'processing_network': processing_network,
            'detailed_rates_and_fees_link': detailed_rates_and_fees_link,
        }

        if issuer.name == 'Discover':
            # For Discover cards, rewards and fees fields should be added
            # Manually. If not removed from dictionary these fields will be
            # overwritten by '' everytime the celery task runs.
            defaults.pop('rewards_bonus')
            defaults.pop('rewards_bonus_terms')
            defaults.pop('detailed_rates_and_fees_link')

            # Update the values with fields specific for discover cards.
            intro_purchase_apr_desc = fields.get('introPurchAPR', '')

            if intro_purchase_apr_desc != 'N/A':
                defaults['intro_purchase_apr'] = '{0}, {1}'.format(
                    intro_purchase_apr_desc,
                    fields.get('introPurchAPRPeriod', '')
                )
            else:
                defaults['intro_purchase_apr'] = 'N/A'

            intro_transfer_apr_desc = fields.get('introTransferAPR', '')

            if intro_transfer_apr_desc != 'N/A':
                defaults['intro_transfer_apr'] = '{0}, {1}'.format(
                    intro_transfer_apr_desc,
                    fields.get('introTransAPRPeriod', '')
                )
            else:
                defaults['intro_transfer_apr'] = 'N/A'

            defaults['transfer_apr'] = defaults['purchase_apr']

        card, created = CreditCard.objects.update_or_create(slug=slug, defaults=defaults)

        if image_source_url:
            card.update_image(image_source_url)


@shared_task
def update_capital_one_cards():
    def get_apr_value(apr_description, apr_period_description):
        if apr_description != 'N/A':
            return "{0} {1}".format(apr_description, apr_period_description)
        else:
            return 'N/A'

    access_token = get_capital_one_access_token()
    latest_capital_one_cards_details = get_capital_one_cards(access_token)['products']

    for latest_card in latest_capital_one_cards_details:
        try:
            card = CreditCard.objects.get(product_id=latest_card['productId'])

            marketing_list_items = ['<li>{0}</li>'.format(
                item) for item in latest_card['marketingCopy']
            ]
            card.marketing_copy = '<ul>\n\t{0}\n\t</ul>'.format(
                '\n'.join(marketing_list_items)
            )
            card.application_link = latest_card['applyNowLink']
            card.name = latest_card['productDisplayName']
            card.credit_rating = '/'.join(latest_card['creditRating'])
            card.annual_fee = latest_card['annualMembershipFee']
            intro_purchase_apr_desc = latest_card['introPurchaseApr']['introPurchaseAprDescription']
            intro_purchase_apr_period_desc = latest_card['introPurchaseAprPeriod']['introPurchaseAprPeriodDescription']
            card.intro_purchase_apr = get_apr_value(intro_purchase_apr_desc, intro_purchase_apr_period_desc)
            card.purchase_apr = latest_card['purchaseApr']['purchaseAprDescription']
            intro_transfer_apr_desc = latest_card['introBalanceTransferApr']['introBalanceTransferAprDescription']
            intro_transfer_apr_period_desc = latest_card['introBalanceTransferAprPeriod']['introBalanceTransferAprPeriodDescription']
            card.intro_transfer_apr = get_apr_value(intro_transfer_apr_desc, intro_transfer_apr_period_desc)
            card.transfer_apr = latest_card['balanceTransferApr']['balanceTransferAprDescription']
            bonus = latest_card['rewards'][0]['rewardsBonus']
            if bonus['rewardsBonusValue'] and bonus['rewardsBonusType']:
                if bonus['rewardsBonusType'] == 'Cash Back':
                    card.rewards_bonus = '${0} {1}'.format(
                        bonus['rewardsBonusValue'], bonus['rewardsBonusType']
                    )
                else:
                    card.rewards_bonus = '{0} {1}'.format(
                        format(bonus['rewardsBonusValue'], ","),
                        bonus['rewardsBonusType']
                    )
            if bonus['rewardsBonusTerms']:
                card.rewards_bonus_terms = bonus['rewardsBonusTerms']
            card.save(update_fields=[
                'name', 'marketing_copy', 'application_link', 'credit_rating',
                'annual_fee', 'intro_purchase_apr', 'purchase_apr',
                'intro_transfer_apr', 'transfer_apr', 'rewards_bonus',
                'rewards_bonus_terms'
            ])
            card.update_image(latest_card['images'][0]['url'])

        except CreditCard.DoesNotExist:
            pass
