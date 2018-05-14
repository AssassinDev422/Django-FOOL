# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditcards', '0018_make_marketing_copy_richtext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='processing_network',
            field=models.IntegerField(null=True, choices=[(1, b'Visa'), (2, b'MasterCard'), (3, b'American Express'), (4, b'Discover')]),
        ),
    ]
