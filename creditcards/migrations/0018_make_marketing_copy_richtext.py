# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('creditcards', '0017_auto_20170119_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='marketing_copy',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
