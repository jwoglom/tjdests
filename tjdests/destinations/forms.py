# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.forms import AuthenticationForm
from django import forms

class AuthenticateForm(AuthenticationForm):

    username = forms.CharField(required=True,
                               widget=forms.widgets.TextInput(attrs={"placeholder": "Username"}),
                               error_messages={"required": "Invalid username",
                                               "inactive": "Access disallowed."})

    password = forms.CharField(required=True,
                               widget=forms.widgets.PasswordInput(attrs={"placeholder": "Password"}),
                               error_messages={"required": "Invalid password",
                                               "inactive": "Access disallowed."})
