# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditcards', '0019_add_discover_processing_network'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcard',
            name='intro_purchase_apr_period_type',
            field=models.TextField(blank=True),
        ),
    ]
