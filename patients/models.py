from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings

from phonenumber_field.modelfields import PhoneNumberField

class Patient(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='patients')
    name = models.CharField(200)
    last_name = models.CharField(200)
    email = models.EmailField(max_length=255, unique=True,)
    conf_email = models.BooleanField(default=False)
    phone_number = PhoneNumberField(region='BR',  unique=True,)
    cep = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name