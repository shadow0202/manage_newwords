# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-09 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show_newwords', '0018_auto_20180426_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coverate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=30)),
                ('coverate', models.CharField(max_length=30)),
            ],
        ),
    ]