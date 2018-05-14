# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('creditcards', '0012_add_detailed_rates_fees_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcardreview',
            name='cons',
            field=wagtail.wagtailcore.fields.RichTextField(default=b'<ul><li></li></ul>'),
        ),
        migrations.AlterField(
            model_name='creditcardreview',
            name='pros',
            field=wagtail.wagtailcore.fields.RichTextField(default=b'<ul><li></li></ul>'),
        ),
    ]
