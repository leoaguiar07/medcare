from django.db import models
from doctors.models import Doctor,Schedule
from patients.models import Patient



class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT, related_name='appointment')
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='appointment')
    schedule = models.ForeignKey(Schedule, on_delete=models.PROTECT, related_name='appointment', default = "")
    # datetime = models.DateTimeField()
    # status = models.CharField(max_length=20)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['doctor']

    def __str__(self):
        return self.patient.name
