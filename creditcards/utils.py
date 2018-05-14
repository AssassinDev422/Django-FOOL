import requests
from logging import getLogger
from django.conf import settings

logger = getLogger(__name__)


def get_capital_one_access_token():
    # Obtaining an access token
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = [
        ('client_id', settings.CAPITAL_ONE_CLIENT_ID),
        ('client_secret', settings.CAPITAL_ONE_CLIENT_SECRET),
        ('grant_type', 'client_credentials'),
    ]

    access_token = requests.post(
        '{0}{1}'.format(settings.CAPITAL_ONE_API_BASE_URI, 'oauth2/token'),
        headers=headers, data=data
    )

    try:
        access_token.raise_for_status()
    except:
        logger.exception('Error fetching access token from Capital One')
        return None

    return access_token.json()['access_token']


def get_capital_one_cards(access_token):
    headers = {
        'Accept': 'application/json;v=3',
        'Authorization': 'Bearer ' + access_token,
        'Accept-Language': 'en-US',
    }

    cards = requests.get(
        '{0}{1}'.format(
            settings.CAPITAL_ONE_API_BASE_URI,
            'credit-offers/products/cards'
        ), headers=headers
    )

    try:
        cards.raise_for_status()
    except:
        logger.exception('Error fetching credit card data from Capital One')
        return None

    return cards.json()


def get_capital_one_latest_card_details(access_token, product_id, card_type):
    headers = {
        'Accept': 'application/json;v=3',
        'Authorization': 'Bearer ' + access_token,
        'Accept-Language': 'en-US',
    }

    card = requests.get(
        '{0}{1}/{2}/{3}'.format(
            settings.CAPITAL_ONE_API_BASE_URI,
            'credit-offers/products/cards', card_type, product_id
        ), headers=headers
    )

    try:
        card.raise_for_status()
    except:
        logger.exception('Error fetching credit card data from Capital One')
        return None

    return card.json()
