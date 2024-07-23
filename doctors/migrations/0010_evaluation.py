# Generated by Django 5.0.6 on 2024-06-08 02:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0009_doctor_price_tele'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='evaluation_doctor', to='doctors.doctor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='evaluation_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['doctor'],
            },
        ),
    ]
