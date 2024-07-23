from django.contrib import admin
from . import models


class PatientAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)




admin.site.register(models.Patient, PatientAdmin)
