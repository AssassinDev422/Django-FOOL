# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import wagtail.wagtailcore.fields
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('creditcards', '0009_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardIssuer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('possessive', models.CharField(max_length=200)),
                ('cj_advertiser_id', models.IntegerField(unique=True, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='creditcard',
            name='processing_network',
            field=models.IntegerField(null=True, choices=[(1, b'Visa'), (2, b'MasterCard'), (3, b'American Express')]),
        ),
        migrations.AddField(
            model_name='creditcard',
            name='rewards_bonus',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='creditcard',
            name='rewards_bonus_terms',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='creditcardreview',
            name='cons',
            field=wagtail.wagtailcore.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='creditcardreview',
            name='pros',
            field=wagtail.wagtailcore.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='creditcard',
            name='issuer',
            field=models.ForeignKey(to='creditcards.CardIssuer', null=True),
        ),
    ]
