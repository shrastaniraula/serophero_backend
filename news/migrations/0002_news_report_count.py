# Generated by Django 4.1.7 on 2024-02-17 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='report_count',
            field=models.IntegerField(default=0),
        ),
    ]
