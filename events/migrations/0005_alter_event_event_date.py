# Generated by Django 4.1.7 on 2024-02-15 04:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_event_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(default=datetime.datetime(2024, 2, 15, 10, 3, 22, 246243)),
        ),
    ]
