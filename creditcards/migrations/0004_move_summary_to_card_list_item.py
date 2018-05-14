# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('creditcards', '0003_auto_20161212_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creditcardreview',
            name='summary',
        ),
        migrations.AddField(
            model_name='creditcardlistitem',
            name='summary',
            field=wagtail.wagtailcore.fields.RichTextField(default=' '),
            preserve_default=False,
        ),
    ]
