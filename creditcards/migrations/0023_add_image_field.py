# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditcards', '0022_remove_broken_out_intro_purchase_apr_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcard',
            name='card_image',
            field=models.ImageField(null=True, upload_to=b'credit-card-art'),
        ),
    ]
