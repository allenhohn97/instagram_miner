# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-07 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ig_miner_app', '0009_auto_20160506_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='End_Date',
            field=models.CharField(help_text=b'MM/DD/YYYY', max_length=10),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='Start_Date',
            field=models.CharField(help_text=b'MM/DD/YYYY', max_length=10),
        ),
    ]
