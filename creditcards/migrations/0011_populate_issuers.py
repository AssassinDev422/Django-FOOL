# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def populate_issuers(apps, schema_editor):
    issuers = [
        {
            'name': 'Bank of America',
            'possessive': "Bank of America's",
            'cj_advertiser_id': 3836079
        },
        {
            'name': 'Barclaycard',
            'possessive': "Barclaycard's",
            'cj_advertiser_id': 4056495
        },
    ]
    CardIssuer = apps.get_model('creditcards', 'CardIssuer')
    for issuer in issuers:
        CardIssuer.objects.update_or_create(cj_advertiser_id=issuer['cj_advertiser_id'], defaults=issuer)


def depopulate_issuers(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('creditcards', '0010_auto_20170113_1450'),
    ]

    operations = [
        migrations.RunPython(populate_issuers, depopulate_issuers)
    ]
