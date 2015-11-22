from django.contrib import admin
from .models import College, CollegeApp, APTest, APExam, User
# Register your models here.
admin.site.register([User,
                     College,
                     CollegeApp,
                     APTest,
                     APExam])