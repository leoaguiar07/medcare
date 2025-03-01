# Generated by Django 5.0.6 on 2024-06-18 05:17

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0013_alter_address_maps_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='cell_phone',
        ),
        migrations.AddField(
            model_name='doctor',
            name='conf_cell',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='doctor',
            name='email',
            field=models.EmailField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='doctor',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128, region='BR'),
        ),
    ]
