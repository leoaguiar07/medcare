from django.contrib import admin
from . import models


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class AddressAdmin(admin.ModelAdmin):
    list_display = ('doctor',)
    search_fields = ('doctor',)


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('id','doctor',)


admin.site.register(models.Doctor, DoctorAdmin)
admin.site.register(models.Address, AddressAdmin)
admin.site.register(models.Schedule, ScheduleAdmin)