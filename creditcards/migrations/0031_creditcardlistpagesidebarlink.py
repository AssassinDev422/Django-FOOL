# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditcards', '0030_creditcardlist_ending'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCardListPageSidebarLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('text', models.CharField(max_length=255)),
                ('categorized_by', models.CharField(max_length=255, choices=[(b'type', b'Type'), (b'issuer', b'Issuer'), (b'creditscore', b'Credit Score')])),
            ],
        ),
    ]
