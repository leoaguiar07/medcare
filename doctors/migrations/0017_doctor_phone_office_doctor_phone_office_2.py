# Generated by Django 5.0.6 on 2024-06-18 15:31

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0016_alter_doctor_email_alter_doctor_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='phone_office',
            field=phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128, region='BR'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='phone_office_2',
            field=phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128, region='BR'),
        ),
    ]
