# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.contrib.table_block.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import banking.models
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0007_auto_20171024_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankingstreamfieldpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), (b'bankrate_widget', banking.models.BankrateWidgetBlock()), (b'bankrate_cd_widget', banking.models.BankrateCDRatesBlock()), (b'bankrate_mortgage_widget', banking.models.BankrateMortgageRatesBlock()), (b'table_block', wagtail.contrib.table_block.blocks.TableBlock(table_options={b'contextMenu': True, b'autoColumnSize': False, b'stretchH': b'all', b'height': 216, b'startRows': 3, b'startCols': 3, b'renderer': b'html', b'minSpareRows': 0, b'language': b'en', b'colHeaders': False, b'editor': b'text', b'rowHeaders': False}))]),
        ),
        migrations.AlterField(
            model_name='bankingstreamfieldpage',
            name='comparisons',
            field=wagtail.wagtailcore.fields.StreamField([(b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), (b'banking_comparison', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock()), (b'body', wagtail.wagtailcore.blocks.RichTextBlock()), (b'url', wagtail.wagtailcore.blocks.URLBlock()), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock())])), (b'bankrate_widget', banking.models.BankrateWidgetBlock()), (b'bankrate_cd_widget', banking.models.BankrateCDRatesBlock()), (b'bankrate_mortgage_widget', banking.models.BankrateMortgageRatesBlock()), (b'table_block', wagtail.contrib.table_block.blocks.TableBlock(table_options={b'contextMenu': True, b'autoColumnSize': False, b'stretchH': b'all', b'height': 216, b'startRows': 3, b'startCols': 3, b'renderer': b'html', b'minSpareRows': 0, b'language': b'en', b'colHeaders': False, b'editor': b'text', b'rowHeaders': False}))], null=True, blank=True),
        ),
    ]
