# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditcards', '0028_auto_20170725_0519'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardissuer',
            name='show_fee_link',
            field=models.BooleanField(default=True, help_text=b'Show detailed rates and fees link for this card issuer'),
        ),
    ]
