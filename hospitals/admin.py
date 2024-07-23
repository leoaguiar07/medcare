from django.contrib import admin
from . import models


class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(models.Hospital, HospitalAdmin)
