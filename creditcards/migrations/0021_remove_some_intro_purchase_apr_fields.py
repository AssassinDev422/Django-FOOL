# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditcards', '0020_add_intro_purchase_apr_period_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creditcard',
            name='intro_purchase_apr',
        ),
        migrations.RemoveField(
            model_name='creditcard',
            name='intro_purchase_apr_period',
        ),
        migrations.RemoveField(
            model_name='creditcard',
            name='intro_purchase_apr_type',
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='intro_purchase_apr_period_type',
            field=models.TextField(help_text=b'e.g. "billing cycles" for 12 billing cycles', blank=True),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='intro_purchase_apr_period_value',
            field=models.TextField(help_text=b'e.g. "12" for 12 billing cycles', blank=True),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='intro_purchase_apr_value',
            field=models.TextField(help_text=b'e.g. "0" for 0%', blank=True),
        ),
    ]
