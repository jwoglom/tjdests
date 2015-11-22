from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import User


def index(request):
    if request.user.is_authenticated():
        return render(request, "login.html", {})
    else:
        return render(request, "login.html", {})

@login_required
def home(request):
    return render(request, "home.html", {})