# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-11 03:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show_newwords', '0022_runinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runinfo',
            name='info',
            field=models.CharField(max_length=128),
        ),
    ]
