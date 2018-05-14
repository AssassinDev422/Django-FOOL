# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('creditcards', '0002_auto_20161212_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcardlistitem',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='items', to='creditcards.CreditCardList'),
        ),
    ]
