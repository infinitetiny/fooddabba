# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 10:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fdmain', '0009_remove_fd_cususer_cuslocation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fd_cususer',
            name='tiffintype',
        ),
    ]
