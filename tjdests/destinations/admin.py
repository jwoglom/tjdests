# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Senior, College, CollegeApp, APExam, SAT2, User
# Register your models here.
admin.site.register([Senior,
                     User,
                     College,
                     CollegeApp,
                     APExam,
                     SAT2])