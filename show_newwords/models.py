# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=200)
    dec = models.CharField(max_length=200)
    status = models.CharField(max_length=200)

    def __unicode__(self):
        return self.task_name


class NewWords(models.Model):
    id = models.AutoField(primary_key=True)
    new_word = models.CharField(max_length=200)
    counts = models.IntegerField()
    types = models.CharField(max_length=200)
    add_msg = models.CharField(max_length=200,blank=True)

    def __unicode__(self):
        return self.new_word

class New_List(models.Model):
    id = models.AutoField(primary_key=True)
    new_word = models.CharField(max_length=200)
    counts = models.IntegerField()
    types = models.CharField(max_length=200)
    add_msg = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.new_word

class Stop_List(models.Model):
    id = models.AutoField(primary_key=True)
    stop_word = models.CharField(max_length=200)
    add_msg = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.stop_word

class Hot_List(models.Model):
    id = models.AutoField(primary_key=True)
    hot_word = models.CharField(max_length=200)
    counts = models.IntegerField()
    types = models.CharField(max_length=200)
    add_msg = models.CharField(max_length=200, blank=True)

class Coverate(models.Model):
    time = models.CharField(max_length=30)
    coverate = models.FloatField(max_length=10)

    def __unicode__(self):
        return str(self.coverate)

class RunTime(models.Model):
    time = models.CharField(max_length=30)


class runInfo(models.Model):
    info = models.CharField(max_length=256)