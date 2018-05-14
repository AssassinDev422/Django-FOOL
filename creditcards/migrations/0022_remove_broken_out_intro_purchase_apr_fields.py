# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditcards', '0021_remove_some_intro_purchase_apr_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creditcard',
            name='intro_purchase_apr_period_type',
        ),
        migrations.RemoveField(
            model_name='creditcard',
            name='intro_purchase_apr_period_value',
        ),
        migrations.RemoveField(
            model_name='creditcard',
            name='intro_purchase_apr_value',
        ),
        migrations.AddField(
            model_name='creditcard',
            name='intro_purchase_apr',
            field=models.TextField(blank=True),
        ),
    ]
