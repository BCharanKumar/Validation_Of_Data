# Generated by Django 5.0.7 on 2024-11-08 05:37

import app.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='semail',
            field=models.EmailField(max_length=254, validators=[app.models.check_for_email]),
        ),
        migrations.AlterField(
            model_name='student',
            name='sname',
            field=models.CharField(max_length=125, validators=[app.models.check_for_char, django.core.validators.MinLengthValidator(6)]),
        ),
    ]
