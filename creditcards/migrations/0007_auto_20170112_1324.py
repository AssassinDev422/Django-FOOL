# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('creditcards', '0006_add_creditcard_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcardreview',
            name='card',
            field=models.OneToOneField(related_name='review', on_delete=django.db.models.deletion.PROTECT, to='creditcards.CreditCard'),
        ),
    ]
