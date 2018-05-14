# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.contrib.table_block.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('creditcards', '0032_creditcardreview_intro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcardreview',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'heading', wagtail.wagtailcore.blocks.CharBlock(classname=b'full title')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'blockquote', wagtail.wagtailcore.blocks.BlockQuoteBlock()), (b'table_block', wagtail.contrib.table_block.blocks.TableBlock())]),
        ),
    ]
