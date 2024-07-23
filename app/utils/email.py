import os
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from .tokens import account_activation_token

def send_activation_email(user, request):
    current_site = get_current_site(request)
    mail_subject = 'Ative sua conta.'
    message = render_to_string('registration/account_activation_email.html', {
        # api_key = os.getenv('GOOGLE_MAPS_API_KEY')
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })
    send_mail(mail_subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
