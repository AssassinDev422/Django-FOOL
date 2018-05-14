# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditcards', '0027_cardissuer_requires_intermediate_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcard',
            name='card_type',
            field=models.CharField(blank=True, help_text=b'Required only if card Issuer is Capital One', max_length=10, choices=[(b'business', b'Business Card'), (b'consumer', b'Consumer Card')]),
        ),
        migrations.AddField(
            model_name='creditcard',
            name='product_id',
            field=models.CharField(help_text=b'Required only if card Issuer is Capital One', max_length=200, blank=True),
        ),
    ]
