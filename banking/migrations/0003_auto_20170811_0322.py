# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0002_bankingpagecomparisonlinks_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bankingindexpage',
            options={'verbose_name': 'Banking and Savings index page'},
        ),
        migrations.AlterModelOptions(
            name='bankingpage',
            options={'verbose_name': 'Banking and Savings page'},
        ),
    ]
