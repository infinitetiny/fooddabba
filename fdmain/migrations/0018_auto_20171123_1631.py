# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 11:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fdmain', '0017_fd_cususer_orderdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fd_cususer',
            name='orderdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 23, 11, 1, 47, 47214, tzinfo=utc), null=True),
        ),
    ]