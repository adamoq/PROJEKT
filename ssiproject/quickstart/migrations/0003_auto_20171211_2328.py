# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_auto_20171211_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientprofile',
            name='birth',
            field=models.DateField(blank=True, default='2000-01-01'),
        ),
    ]
