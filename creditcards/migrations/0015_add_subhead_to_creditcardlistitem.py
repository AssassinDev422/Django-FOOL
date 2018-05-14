# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditcards', '0014_rename_possessive_to_possessive_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcardlistitem',
            name='subhead',
            field=models.CharField(help_text=b'Optional subhead for grouping cards on the page', max_length=255, blank=True),
        ),
    ]
