# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-06 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ig_miner_app', '0007_auto_20160506_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='campaign_title',
        ),
        migrations.AddField(
            model_name='photo',
            name='campaign_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]