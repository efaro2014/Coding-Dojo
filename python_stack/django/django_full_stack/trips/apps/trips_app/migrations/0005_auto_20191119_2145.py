# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-20 05:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trips_app', '0004_auto_20191119_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
