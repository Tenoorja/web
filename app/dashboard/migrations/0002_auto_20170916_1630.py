# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-16 23:30
from __future__ import unicode_literals

import datetime
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bounty',
            name='bounty_owner_address',
            field=models.CharField(default='0x0', max_length=30),
        ),
        migrations.AddField(
            model_name='bounty',
            name='claimeee_address',
            field=models.CharField(default='0x0', max_length=30),
        ),
        migrations.AddField(
            model_name='bounty',
            name='expires_date',
            field=models.DateField(default=datetime.datetime(2017, 9, 16, 23, 30, 30, 669947, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='bounty',
            name='github_url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='bounty',
            name='is_open',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bounty',
            name='raw_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
        ),
    ]