# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.debug import sensitive_post_parameters
from .models import User, Senior, College
from .forms import UserForm
from .email import verify_email


def index_view(request):
    if request.user.is_authenticated():
        return home_view(request)
    else:
        return login_view(request)

@sensitive_post_parameters("password")
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if not user.verified:
                logout(request)
                return redirect("/?unverified=1")
            login(request, user)
            return redirect("/?")
    else:
        form = AuthenticationForm()

    context = {
        "form": form
    }

    return render(request, "login.html", context)

def register_view(request):
    if request.method == "POST":
        form = UserForm(data=request.POST)
        if form.is_valid():
            obj = form.save()
            name = "{} {}".format(obj.first_name, obj.last_name)
            verify_email(request, obj.username, name, obj.verify_key)
            obj.save()

            return redirect("/?verify=1")
    else:
        form = UserForm()

    context = {
        "form": form
    }
    return render(request, "register.html", context)

def verify_view(request, verify_key):
    user = get_object_or_404(User, verify_key=verify_key)
    if not user.verified:
        user.verified = True
        user.verify_key = None
        user.save()
        return redirect("/?verified=1")
    return redirect("/")


def logout_view(request):
    logout(request)
    return redirect("/")

@login_required
def home_view(request):
    return render(request, "home.html", {})

@login_required
def students_view(request):
    students = Senior.objects.all()
    context = {
        "students": students
    }
    return render(request, "students.html", context)

@login_required
def colleges_view(request):
    colleges = College.objects.exclude(collegeapp__isnull=True)
    context = {
        "colleges": colleges
    }
    return render(request, "colleges.html", context)

@login_required
def destinations_view(request):
    students = Senior.objects.all()
    context = {
        "students": students
    }
    return render(request, "destinations.html", context)

@login_required
def student_view(request, student_id):
    student = get_object_or_404(Senior, id=student_id)
    context = {
        "student": student
    }
    return render(request, "student.html", context)