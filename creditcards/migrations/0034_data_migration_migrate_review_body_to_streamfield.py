# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from wagtail.wagtailcore.rich_text import RichText


def convert_to_streamfield(apps, schema_editor):
    ReviewPage = apps.get_model("creditcards", "CreditCardReview")
    for page in ReviewPage.objects.all():
        if page.body.raw_text and not page.body:
            page.body = [('paragraph', RichText(page.body.raw_text))]
            page.save()


def convert_to_richtext(apps, schema_editor):
    ReviewPage = apps.get_model("creditcards", "CreditCardReview")
    for page in ReviewPage.objects.all():
        if page.body.raw_text is None:
            raw_text = ''.join([
                child.value.source for child in page.body
                if child.block_type == 'paragraph'
            ])
            page.body = raw_text
            page.save()


class Migration(migrations.Migration):

    dependencies = [
        # leave the dependency line from the generated migration intact!
        ('creditcards', '0033_auto_20171211_0421'),
    ]

    operations = [
        migrations.RunPython(
            convert_to_streamfield,
            convert_to_richtext,
        ),
    ]
