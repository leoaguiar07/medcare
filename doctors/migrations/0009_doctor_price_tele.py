# Generated by Django 5.0.6 on 2024-06-05 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0008_alter_address_district'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='price_tele',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
    ]
