# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.contrib.table_block.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('creditcards', '0029_cardissuer_show_fee_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcardlist',
            name='ending',
            field=wagtail.wagtailcore.fields.StreamField([(b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), (b'table_block', wagtail.contrib.table_block.blocks.TableBlock())], blank=True),
        ),
    ]
