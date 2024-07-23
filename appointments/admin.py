from django.contrib import admin
from . import models


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('doctor',)
    search_fields = ('doctor',)


admin.site.register(models.Appointment, AppointmentAdmin)
