from django.test import TestCase

from creditcards.templatetags.creditcards_tags import append_source
from creditcards.models import CreditCard, CardIssuer


class _RequestWithUtmTokens(object):
    @property
    def utm_tokens(self):
        return type("UtmTokens", (object,), {'source': 'source'})()


class AppendParamsTestCase(TestCase):
    def setUp(self):
        self.context = {
            'request': _RequestWithUtmTokens(),
        }

    def test_append_link_params(self):
        link = 'https://fool.com?a=1'
        issuers = [
            # sid
            ('Bank of America', 'https://fool.com?a=1&sid=source'),
            ('Barclaycard', 'https://fool.com?a=1&sid=source'),
            ('Discover', 'https://fool.com?a=1&sid=source'),
            ('Citi', 'https://fool.com?a=1&sid=source'),
            ('Amex', 'https://fool.com?a=1&sid=source'),
            # u1
            ('Chase', 'https://fool.com?a=1&u1=source'),
            #subid1
            ('Capital One', 'https://fool.com?a=1&subid1=source'),
        ]

        for issuer_name, expected in issuers:

            card_issuer, _ = CardIssuer.objects.get_or_create(name=issuer_name)
            card = CreditCard.objects.create(name=issuer_name, issuer=card_issuer)
            self.context['card'] = card

            self.assertEqual(expected, append_source(self.context, link))
