from django.db import models

class Hospital(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    cep = models.IntegerField()
    address = models.CharField(max_length=255)
    add = models.CharField(max_length=255)
    number = models.IntegerField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    payment_type = models.CharField(max_length=255)
    insurances = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

