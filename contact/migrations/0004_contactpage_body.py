# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20170906_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'heading', wagtail.wagtailcore.blocks.CharBlock(classname=b'full title')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'blockquote', wagtail.wagtailcore.blocks.BlockQuoteBlock()), (b'raw_html', wagtail.wagtailcore.blocks.RawHTMLBlock())], blank=True),
        ),
    ]
