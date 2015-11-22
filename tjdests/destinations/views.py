# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.debug import sensitive_post_parameters
from .models import User, Senior
from .forms import AuthenticateForm


def index_view(request):
    if request.user.is_authenticated():
        return home_view(request)
    else:
        return login_view(request)

@sensitive_post_parameters("password")
def login_view(request):
    if request.method == "POST":
        form = AuthenticateForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("/")
    else:
        form = AuthenticateForm()

    context = {
        "form": form
    }

    return render(request, "login.html", context)


def logout_view(request):
    logout()
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
def student_view(request, student_id):
    student = get_object_or_404(Senior, id=student_id)
    context = {
        "student": student
    }
    return render(request, "student.html", context)