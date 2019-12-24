# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-20 01:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trips_app', '0002_remove_user_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=45)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('Plan', models.CharField(max_length=45)),
                ('planner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planned_trips', to='trips_app.User')),
            ],
        ),
    ]
