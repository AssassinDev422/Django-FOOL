# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditcards', '0004_move_summary_to_card_list_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcardlistitem',
            name='card',
            field=models.ForeignKey(related_name='card_list_items', to='creditcards.CreditCard'),
        ),
    ]
