# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailembeds.blocks
import about.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0033_remove_golive_expiry_help_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.StreamField([(b'banner', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'heading', about.models.HeadingBlock()), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), (b'video', wagtail.wagtailembeds.blocks.EmbedBlock()), (b'awards', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'badge', wagtail.wagtailimages.blocks.ImageChooserBlock())], label=b'awards'), template=b'about/blocks/awards_list.html'))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
