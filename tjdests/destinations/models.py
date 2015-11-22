from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class College(models.Model):
    name = models.CharField(max_length=1000)
    ceeb = models.IntegerField(unique=True)


class CollegeApp(models.Model):
    college = models.ForeignKey("College")
    program = models.CharField(max_length=250)
    user = models.ForeignKey("User")
    attending = models.BooleanField()
    TYPES = (
        ("RD", "Regular Decision"),
        ("ED", "Early Decision"),
        ("EA", "Early Action"),
        ("PR", "Priority")
    )
    applied = models.CharField(max_length=2, choices=TYPES, default="RD")
    RESULTS = (
        ("NA", "Unknown")
        ("AC", "Accepted"),
        ("RJ", "Rejected"),
        ("WL", "Waitlisted"),
        ("DF", "Deferred")
    )
    result = models.CharField(max_length=2, choices=TYPES, default="NA")
    submitted = models.DateField(required=False)
    notified = models.DateField(required=False)
    legacy = models.BooleanField(default=False)
    interview = models.BooleanField(default=False)
    recruited = models.CharField(max_length=100)
    supplement = models.CharField(max_length=100)
    comments = models.CharField(max_length=1000)


class APTest(models.Model):
    name = models.CharField(max_length=100)


class APExam(models.Model):
    aptest = models.ForeignKey("APTest")
    user = models.ForeignKey("User")
    score = models.IntegerField(max_value=5, min_value=0)
    year = models.IntegerField(max_value=3000, min_value=0)
    took_class = models.BooleanField(default=True)


class User(AbstractBaseUser):
    USERNAME_FIELD = "username"
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField()
    last_name = models.CharField()
    email = models.CharField(max_length=100, required=False)
    gender = models.CharField(max_length=1, choices=(("M", "Male"), ("F", "Female")))
    race = models.CharField(max_length=20)
    hispanic = models.BooleanField()
    international = models.BooleanField()

    gpa = models.DecimalField(max_digits=4, decimal_places=3)
    sat2400 = models.IntegerField(max_value=2400, min_value=0)
    sat1600 = models.IntegerField(max_value=1600, min_value=0)
    act = models.IntegerField(max_value=36, min_value=0)
    honors = models.CharField(max_length=1000)
    
    colleges = models.ManyToManyField("College", through="CollegeApp")
    aps = models.ManyToManyField("APTest", through="APExam")