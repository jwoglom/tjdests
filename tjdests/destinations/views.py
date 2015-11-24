# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.debug import sensitive_post_parameters
from .models import User, Senior, College
from .forms import UserForm, SeniorForm, CollegeAppForm
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
def update_view(request):
    if not request.user.is_senior:
        return redirect("/")

    updated = None

    senior = request.user.senior

    if request.method == "POST":
        if senior:
            form = SeniorForm(instance=senior, data=request.POST)
        else:
            form = SeniorForm(data=request.POST)

        if form.is_valid():
            obj = form.save()
            user = request.user
            user.senior = obj
            user.save()
            senior = request.user.senior
            updated = True
    elif senior:
        form = SeniorForm(instance=senior)
    else:
        form = SeniorForm()

    context = {
        "form": form,
        "senior": senior,
        "updated": updated
    }
    return render(request, "update.html", context)

@login_required
def update_school_view(request, app_id=None):
    if not request.user.is_senior:
        return redirect("/")

    updated = None

    senior = request.user.senior

    app = None
    if app_id:
        app = get_object_or_404(CollegeApp, id=app_id)


    if request.method == "POST":
        if app:
            form = CollegeAppForm(instance=app, data=request.POST)
        else:
            form = CollegeAppForm(data=request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.senior = senior
            obj.save()
            updated = True
    elif senior:
        form = CollegeAppForm(instance=app)
    else:
        form = CollegeAppForm()

    context = {
        "form": form,
        "senior": senior,
        "app": app,
        "updated": updated
    }
    return render(request, "update_school.html", context)

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