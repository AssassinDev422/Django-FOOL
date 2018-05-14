# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditcards', '0013_set_defaults_for_pros_cons'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardissuer',
            old_name='possessive',
            new_name='possessive_name',
        ),
    ]
