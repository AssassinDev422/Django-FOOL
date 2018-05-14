# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditcards', '0026_remove_image_source_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardissuer',
            name='requires_intermediate_page',
            field=models.BooleanField(default=False),
        ),
    ]
