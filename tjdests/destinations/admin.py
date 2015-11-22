# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import College, CollegeApp, APExam, SAT2, User
# Register your models here.
admin.site.register([User,
                     College,
                     CollegeApp,
                     APExam,
                     SAT2])