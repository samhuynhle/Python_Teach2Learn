# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-28 00:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment_app', '0017_auto_20190827_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 27, 17, 11, 5, 708428)),
        ),
    ]
