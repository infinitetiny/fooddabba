# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fdmain', '0003_delete_fd_cususer'),
    ]

    operations = [
        migrations.CreateModel(
            name='fd_cususer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactnumber', models.CharField(max_length=70, null=True)),
            ],
        ),
    ]