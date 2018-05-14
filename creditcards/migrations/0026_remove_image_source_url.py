# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditcards', '0025_rename_card_image_to_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creditcard',
            name='image_source_url',
        ),
    ]
