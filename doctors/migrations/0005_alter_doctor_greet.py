# Generated by Django 5.0.6 on 2024-05-28 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0004_doctor_greet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='greet',
            field=models.CharField(max_length=5),
        ),
    ]
