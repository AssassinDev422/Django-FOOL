# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditcards', '0023_add_image_field'),
    ]

    operations = [
        migrations.RenameField(
            model_name='creditcard',
            old_name='image',
            new_name='image_source_url',
        ),
    ]
