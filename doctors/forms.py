from django import forms
from . import models


class DoctorForm(forms.ModelForm):
    model = models.Doctor
    fields = ['name','state']