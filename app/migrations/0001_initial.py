# Generated by Django 5.0.7 on 2024-11-08 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sname', models.CharField(max_length=125)),
                ('sid', models.IntegerField(primary_key=True, serialize=False)),
                ('semail', models.EmailField(max_length=254)),
            ],
        ),
    ]