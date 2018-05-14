# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditcards', '0005_auto_20161213_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcard',
            name='annual_fee',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='creditcard',
            name='application_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='creditcard',
            name='credit_rating',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='creditcard',
            name='image',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='creditcard',
            name='intro_purchase_apr',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='creditcard',
            name='intro_transfer_apr',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='creditcard',
            name='marketing_copy',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='creditcard',
            name='purchase_apr',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='creditcard',
            name='transfer_apr',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='name',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]
