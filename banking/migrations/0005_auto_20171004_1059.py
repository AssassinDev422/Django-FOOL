# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0004_bankingstreamfieldpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankingstreamfieldpage',
            name='comparisons',
            field=wagtail.wagtailcore.fields.StreamField([(b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), (b'banking_comparison', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock()), (b'body', wagtail.wagtailcore.blocks.RichTextBlock()), (b'url', wagtail.wagtailcore.blocks.URLBlock()), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock())]))], null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='bankingstreamfieldpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), (b'bankrate_widget', wagtail.wagtailcore.blocks.StructBlock([]))]),
        ),
    ]
