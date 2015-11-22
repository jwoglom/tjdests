# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class College(models.Model):
    name = models.CharField(max_length=1000)
    ceeb = models.IntegerField(unique=True)

    def __unicode__(self):
        return "{}".format(self.name)

    class Meta:
        ordering = ["name"]


class CollegeApp(models.Model):
    college = models.ForeignKey("College")
    program = models.CharField(max_length=250)
    senior = models.ForeignKey("Senior")
    attending = models.BooleanField()
    TYPES = (
        ("RD", "Regular Decision"),
        ("ED", "Early Decision"),
        ("EA", "Early Action"),
        ("PR", "Priority")
    )
    applied = models.CharField(max_length=2, choices=TYPES, default="RD")
    RESULTS = (
        ("NA", "Applied"),
        ("AT", "Attending"),
        ("AC", "Accepted"),
        ("RJ", "Rejected"),
        ("WL", "Waitlisted"),
        ("DF", "Deferred")
    )
    result = models.CharField(max_length=2, choices=RESULTS, default="NA")
    submitted = models.DateField(blank=True)
    notified = models.DateField(blank=True)
    legacy = models.BooleanField(default=False)
    interview = models.BooleanField(default=False)
    deferred = models.BooleanField(default=False)
    waitlisted = models.BooleanField(default=False)
    recruited = models.CharField(max_length=100, blank=True)
    supplement = models.CharField(max_length=100, blank=True)
    comments = models.CharField(max_length=1000, blank=True)

    @property
    def applied_name(self):
        types = {i[0]: i[1] for i in self.TYPES}
        return types[self.applied] if self.applied in types else ""

    @property
    def result_name(self):
        results = {i[0]: i[1] for i in self.RESULTS}
        return results[self.result] if self.result in results else ""
    
    

    def __unicode__(self):
        return "{}".format(self.college)


class APExam(models.Model):
    EXAMS = ("Art History",
             "Music Theory",
             "Studio Art 2D",
             "Studio Art 3D",
             "Studio Art Drawing",
             "Lang",
             "Lit",
             "Comparative Govt",
             "European History",
             "Human Geography",
             "Macroeconomics",
             "Microeconomics",
             "Psychology",
             "US Government",
             "US History",
             "World History",
             "Calculus AB",
             "Calculus BC",
             "Comp Sci A",
             "Comp Sci Principles",
             "Statistics",
             "Biology",
             "Chemistry",
             "Environmental Science",
             "Physics C E&M",
             "Physics C Mech",
             "Physics 1",
             "Physics 2",
             "Chinese",
             "French",
             "German",
             "Italian",
             "Japanese",
             "Latin",
             "Spanish Lang",
             "Spanish Lit")
    name = models.CharField(max_length=100, choices=[(i, i) for i in EXAMS])
    senior = models.ForeignKey("Senior")
    score = models.IntegerField()
    year = models.IntegerField()
    took_class = models.BooleanField(default=True)

    def __unicode__(self):
        return "{} ({})".format(self.name, self.score)


class SAT2(models.Model):
    EXAMS = ("Literature",
             "US History",
             "World History",
             "Math Level 1",
             "Math Level 2",
             "Biology/EM",
             "Chemistry",
             "Physics",
             "French",
             "French Listening",
             "German",
             "German Listening",
             "Spanish",
             "Spanish Listening",
             "Modern Hebrew",
             "Italian",
             "Latin",
             "Chinese Listening",
             "Japanese Listening",
             "Korean Listening")
    name = models.CharField(max_length=100, choices=[(i, i) for i in EXAMS])
    senior = models.ForeignKey("Senior")
    score = models.IntegerField()
    year = models.IntegerField()

    def __unicode__(self):
        return "{} ({})".format(self.name, self.score)


class User(AbstractBaseUser):
    USERNAME_FIELD = "username"
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    senior = models.OneToOneField("Senior", null=True)

    def __unicode__(self):
        return "{} {} ({})".format(self.first_name, self.last_name, self.username)

class Senior(models.Model):
    email = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=1, choices=(("M", "Male"), ("F", "Female")))
    race = models.CharField(max_length=20)
    hispanic = models.BooleanField()
    international = models.BooleanField()

    gpa = models.DecimalField(max_digits=4, decimal_places=3, default=0.00)
    sat2400 = models.IntegerField(default=0)
    sat1600 = models.IntegerField(default=0)
    act = models.IntegerField(default=0)
    honors = models.CharField(max_length=1000)

    colleges = models.ManyToManyField("College", through="CollegeApp")

    def __unicode__(self):
        return "{}".format(self.user)