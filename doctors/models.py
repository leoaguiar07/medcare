from django.db import models
from specialties.models import Specialty
from hospitals.models import Hospital 
# from django.contrib.auth.models import User
from django.conf import settings

from phonenumber_field.modelfields import PhoneNumberField


class Doctor(models.Model):
    specialty = models.ForeignKey(Specialty, on_delete=models.PROTECT, related_name='doctors')
    hospital = models.ForeignKey(Hospital, on_delete=models.PROTECT, related_name='doctors')
    # user = models.ForeignKey(User, on_delete=models.PROTECT,related_name='doctors')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,related_name='doctors')
    photo = models.ImageField(upload_to='doctor', blank=True, null=True)
    greet = models.CharField(max_length=5)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    conf_email = models.BooleanField(default=False)
    phone_number = PhoneNumberField(region='BR',  unique=True)
    phone_office = PhoneNumberField(region='BR',default="")
    phone_office_2 = PhoneNumberField(region='BR', default="")
    conf_cell = models.BooleanField(default=False)
    site = models.CharField(max_length=255)
    ident = models.CharField(max_length=20)
    cr = models.CharField(max_length=50)
    payment_type = models.CharField(max_length=255)
    insurances = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    price_tele = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tele_consultation = models.BooleanField(default=False)
    local_consultation = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

  
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Address(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT,related_name='address')
    cep = models.IntegerField()
    address = models.CharField(max_length=255)
    add = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    number = models.IntegerField()
    maps_link = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
  
    class Meta:
        ordering = ['cep']

    def __str__(self):
        return self.doctor.name


class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT,related_name='schedule')
    datetime = models.DateTimeField()
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['datetime']

    def __str__(self):
        return self.doctor.name


class Evaluation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT,related_name='evaluations')
    # user = models.ForeignKey(User, on_delete=models.PROTECT,related_name='evaluation_user')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,related_name='evaluation_user')
    result = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['doctor']

    def __str__(self):
        return self.doctor.name




    