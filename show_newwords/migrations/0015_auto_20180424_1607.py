# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-24 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show_newwords', '0014_auto_20180424_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_list',
            name='add_msg',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='new_list',
            name='types',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='newwords',
            name='add_msg',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='stop_list',
            name='add_msg',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
