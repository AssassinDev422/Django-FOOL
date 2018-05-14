

from django import template

from www.utils import update_url_query
from creditcards.models import CreditCardListPageSidebarLink

register = template.Library()


@register.simple_tag(takes_context=True)
def append_source(context, link):
    """ Should update link with sid, subid1 or u1 params, based on captured utm source and CreditCard issuer """

    request = context['request']
    source = request.utm_tokens.source

    if not source:
        return link

    # Populate different tracking params based on card issuer
    card = context.get('card')
    if not card or not card.issuer:
        return link

    issuer_name = card.issuer.name
    if issuer_name in ['Bank of America', 'Barclaycard', 'Discover', 'Citi', 'Amex']:
        params = [('sid', source), ]
    elif issuer_name == 'Chase':
        params = [('u1', source), ]
    elif issuer_name == 'Capital One':
        params = [('subid1', source), ]
    else:
        # Fallback to default
        params = [
            ('subid1', source),
            ('sid', source),
            ('u1', source),
        ]

    link += '?' if '?' not in link else ''

    for k, v in params:
        link += '&{0}={1}'.format(k, v)

    return link


@register.inclusion_tag('creditcards/tags/creditcards_list_sidebar.html', takes_context=True)
def creditcards_list_sidebar(context):
    return {
        'links_by_type': CreditCardListPageSidebarLink.objects.filter(
            categorized_by='type'),
        'links_by_issuer': CreditCardListPageSidebarLink.objects.filter(
            categorized_by='issuer'),
        'links_by_creditscore': CreditCardListPageSidebarLink.objects.filter(
            categorized_by='creditscore'),
        'request': context['request'],
    }
