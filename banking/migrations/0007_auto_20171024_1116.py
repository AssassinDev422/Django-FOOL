# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0006_auto_20171023_1251'),
        ('pages', '0004_data_migration_migrate_default_model_to_extended_image_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankingpagecomparisonlinks',
            name='image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='pages.ExtendedImage', null=True),
        ),
    ]
