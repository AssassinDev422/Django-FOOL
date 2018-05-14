# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditcards', '0007_add_slug_to_creditcard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='slug',
            field=models.SlugField(unique=True, max_length=200, editable=False),
        ),
    ]
