# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('creditcards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCardListItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('card', models.ForeignKey(to='creditcards.CreditCard')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='creditcardlist',
            name='cards',
        ),
        migrations.AddField(
            model_name='creditcardlistitem',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='cards', to='creditcards.CreditCardList'),
        ),
    ]
