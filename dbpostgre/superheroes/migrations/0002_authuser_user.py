# Generated by Django 5.1.1 on 2024-10-04 19:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superheroes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authuser',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
