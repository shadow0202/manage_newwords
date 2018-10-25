# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

# Register your models here.
from show_newwords.models import NewWords, Stop_List, Coverate

admin.site.register(NewWords)
admin.site.register(Stop_List)
admin.site.register(Coverate)