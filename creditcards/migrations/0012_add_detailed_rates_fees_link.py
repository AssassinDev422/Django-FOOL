# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditcards', '0011_populate_issuers'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcard',
            name='detailed_rates_and_fees_link',
            field=models.URLField(blank=True),
        ),
    ]
