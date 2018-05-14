# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditcards', '0024_rename_image_to_image_source_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='creditcard',
            old_name='card_image',
            new_name='image',
        ),
    ]
