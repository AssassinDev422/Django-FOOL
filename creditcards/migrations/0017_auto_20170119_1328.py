# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditcards', '0016_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcard',
            name='intro_purchase_apr_period',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='creditcard',
            name='intro_purchase_apr_period_value',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='creditcard',
            name='intro_purchase_apr_type',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='creditcard',
            name='intro_purchase_apr_value',
            field=models.TextField(blank=True),
        ),
    ]
