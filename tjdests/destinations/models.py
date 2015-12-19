# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core import exceptions
from django.db import models

class College(models.Model):
    name = models.CharField(max_length=1000)
    ceeb = models.IntegerField(unique=True)

    def __unicode__(self):
        return "{}: {}".format(self.ceeb, self.name)

    @property
    def applied_set(self):
        return self.collegeapp_set.all()

    @property
    def attending_set(self):
        return self.collegeapp_set.filter(attending=True)

    @property
    def accepted_set(self):
        return self.collegeapp_set.filter(result="AC")

    @property
    def rejected_set(self):
        return self.collegeapp_set.filter(result="RJ")

    @property
    def waitlisted_set(self):
        return self.collegeapp_set.filter(waitlisted=True)

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
        ("PR", "Priority"),
        ("RL", "Rolling Admission")
    )
    applied = models.CharField(max_length=2, choices=TYPES, default="RD")
    RESULTS = (
        ("NA", "Applied"),
        ("AC", "Accepted"),
        ("RJ", "Rejected")
    )
    result = models.CharField(max_length=2, choices=RESULTS, default="NA")
    submitted = models.DateField(null=True, blank=True)
    notified = models.DateField(null=True, blank=True)
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
             "English Language",
             "English Literature",
             "Comparative Govt",
             "European History",
             "Human Geography",
             "Macroeconomics",
             "Microeconomics",
             "Psychology",
             "US Government/Politics",
             "US History",
             "World History",
             "Calculus AB",
             "Calculus BC",
             "Computer Science A",
             #"CS Principles",
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

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **kwargs):
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **kwargs):
        user = self.model(username=username, is_staff=True, is_superuser=True, **kwargs)
        user.set_password(password)
        user.save()
        return user

class User(AbstractBaseUser):
    objects = UserManager()

    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    senior = models.OneToOneField("Senior", null=True)
    verified = models.BooleanField(default=False)
    verify_key = models.CharField(max_length=50, null=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "username"

    def get_full_name(self):
        return self.fullname

    def get_short_name(self):
        return self.shortname

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_admin(self):
        return self.is_staff

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def is_senior(self):
        return self.username.startswith('2016')
    
    

    def __unicode__(self):
        return "{} {} ({})".format(self.first_name, self.last_name, self.username)

    class Meta:
        ordering = ["last_name", "first_name"]

class Senior(models.Model):
    email = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=1, choices=(("M", "Male"), ("F", "Female")))
    RACES = [(i, i) for i in (
        "White",
        "Asian",
        "Black",
        "Hispanic",
        "Indian/AK Native",
        "Multiracial"
    )]
    race = models.CharField(max_length=20, choices=RACES)
    hispanic = models.BooleanField()
    international = models.BooleanField()

    gpa = models.DecimalField(max_digits=4, decimal_places=3, default=0.00)
    sat2400 = models.IntegerField(default=0)
    sat1600 = models.IntegerField(default=0)
    act = models.IntegerField(default=0)
    honors = models.CharField(max_length=1000, blank=True)

    colleges = models.ManyToManyField("College", through="CollegeApp")

    @property
    def attending_college(self):
        att = self.collegeapp_set.filter(attending=True)
        if att:
            return att[0]
        return None

    @property
    def sat(self):
        return self.sat2400 if self.sat2400 else self.sat1600

    def __unicode__(self):
        try:
            return "{}".format(self.user)
        except Exception:
            return "{}".format(self.email)