# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-24 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show_newwords', '0011_auto_20180418_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newwords',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
