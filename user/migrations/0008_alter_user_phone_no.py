# Generated by Django 4.1.7 on 2024-04-01 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_delete_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_no',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
    ]
