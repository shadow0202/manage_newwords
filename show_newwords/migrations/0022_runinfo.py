# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-11 03:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show_newwords', '0021_runtime'),
    ]

    operations = [
        migrations.CreateModel(
            name='runInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=30)),
            ],
        ),
    ]