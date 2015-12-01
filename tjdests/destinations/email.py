# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.template.loader import get_template
from tjdests import settings


def verify_email(request, username, name, verify_key):
    email = "{}@tjhsst.edu".format(username)
    subject = "TJ Destinations Account Verification"
    verify_url = request.build_absolute_uri(reverse('verify', args=[verify_key]))
    if "127.0.0.1:2016" in verify_url:
        verify_url = verify_url.replace("127.0.0.1:2016", "www.tjhsst2016.com")
        verify_url = verify_url.replace("http://", "https://")
    data = {
        "username": username,
        "name": name,
        "verify_url": verify_url
    }

    email_send("email/verify.txt",
               "email/verify.html",
               data,
               subject,
               [email])


def email_send(text_template, html_template, data, subject, emails, headers=None):
    """
        Send an HTML/Plaintext email with the following fields.

        text_template: URL to a Django template for the text email's contents
        html_template: URL to a Django tempalte for the HTML email's contents
        data: The context to pass to the templates
        subject: The subject of the email
        emails: The addresses to send the email to
        headers: A dict of additional headers to send to the message

    """

    text = get_template(text_template)
    html = get_template(html_template)
    text_content = text.render(data)
    html_content = html.render(data)
    headers = {} if headers is None else headers
    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_FROM, emails, headers=headers)
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    return msg