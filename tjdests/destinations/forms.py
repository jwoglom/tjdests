# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from captcha.fields import CaptchaField
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import College, CollegeApp, APExam, SAT2, Senior, User

class CollegeForm(forms.ModelForm):

    class Meta:
        model = College
        fields = ["name",
                  "ceeb"]

class CollegeAppForm(forms.ModelForm):
    comments = forms.CharField(widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        super(CollegeAppForm, self).__init__(*args, **kwargs)
        self.fields["college"].help_text = "Click in the field to search by school name or College Board CEEB number"

    class Meta:
        model = CollegeApp
        fields = ["college",
                  "program",
                  "applied",
                  "submitted",
                  "notified",
                  "result",
                  "attending",
                  "legacy",
                  "interview",
                  "deferred",
                  "waitlisted",
                  "recruited",
                  "supplement",
                  "comments"]

class APExamForm(forms.ModelForm):
    score = forms.IntegerField(max_value=5, min_value=1, widget=forms.NumberInput(attrs={"max": 5, "min": 1, "placeholder": 1}))
    year = forms.IntegerField(max_value=2016, min_value=2013, widget=forms.NumberInput(attrs={"max": 2016, "min": 2013, "placeholder": 2015}))
    class Meta:
        model = APExam
        fields = ["name",
                  "score",
                  "year",
                  "took_class"]

class SAT2Form(forms.ModelForm):
    score = forms.IntegerField(max_value=800, min_value=200, widget=forms.NumberInput(attrs={"max": 800, "min": 1, "placeholder": 200}))
    year = forms.IntegerField(max_value=2016, min_value=2013, widget=forms.NumberInput(attrs={"max": 2016, "min": 2013, "placeholder": 2015}))

    class Meta:
        model = SAT2
        fields = ["name",
                  "score",
                  "year"]

class SeniorForm(forms.ModelForm):
    gpa = forms.DecimalField(max_value=5.0, min_value=0.0, max_digits=4, decimal_places=3)
    sat2400 = forms.IntegerField(max_value=2400, min_value=0)
    sat1600 = forms.IntegerField(max_value=1600, min_value=0)
    act = forms.IntegerField(max_value=36, min_value=0)
    honors = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(SeniorForm, self).__init__(*args, **kwargs)
        self.fields["email"].label = "Other Email"
        self.fields["email"].help_text = "(Optional)"
        self.fields["gpa"].label = "GPA"
        self.fields["sat2400"].label = "SAT (2400 Scale)"
        self.fields["sat1600"].label = "SAT (1600 Scale)"
        self.fields["act"].label = "ACT"
        for i in ["gpa", "sat2400", "sat1600"]:
            self.fields[i].help_text = "Not required, enter 0"
        self.fields["honors"].label = "Honors/Extracurr's"

    class Meta:
        model = Senior
        fields = ["gender",
                  "email",
                  "race",
                  "hispanic",
                  "international",
                  "gpa",
                  "sat2400",
                  "sat1600",
                  "act",
                  "honors"]

class UserForm(UserCreationForm):
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields["username"].label = "TJ Username"
        self.fields["username"].help_text = "e.x. 2016jwoglom"
        self.fields["password1"].help_text = "Do NOT use your TJHSST password."

    def save(self, commit=True):
        obj = super(UserForm, self).save(commit=False)
        obj.verified = False
        verify_key = str(uuid.uuid4())
        obj.verify_key = verify_key
        if commit:
            obj.save()
        return obj

    class Meta:
        model = User
        fields = ["first_name",
                  "last_name",
                  "username",
                  "password1",
                  "password2",
                  "captcha"]
