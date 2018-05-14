# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from ..models import CreditCard as CardModel


def populate_slugs(apps, schema_editor):
    CreditCard = apps.get_model('creditcards', 'CreditCard')
    for card in CreditCard.objects.all():
        card.name, card.slug = CardModel.get_name_and_slug(card.name)
        card.save()


def depopulate_slugs(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('creditcards', '0006_add_creditcard_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcard',
            name='slug',
            field=models.SlugField(default='card-slug', max_length=200, editable=False),
            preserve_default=False,
        ),
        migrations.RunPython(populate_slugs, depopulate_slugs)
    ]
