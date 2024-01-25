# Generated by Django 4.1.7 on 2024-01-07 01:22

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='images',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(blank=True, upload_to='business_images/'), blank=True, null=True, size=None),
        ),
    ]
