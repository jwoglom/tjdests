# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.debug import sensitive_post_parameters
from .models import User, Senior
from .forms import AuthenticateForm


def index(request):
    if request.user.is_authenticated():
        return home(request)
    else:
        return login(request)

@sensitive_post_parameters("password")
def login(request):
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


def logout(request):
    logout()
    return redirect("/")

@login_required
def home(request):
    return render(request, "home.html", {})

@login_required
def students(request):
    students = Senior.objects.all()
    context = {
        "students": students
    }
    return render(request, "students.html", context)