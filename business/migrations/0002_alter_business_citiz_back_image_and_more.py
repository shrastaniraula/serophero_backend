# Generated by Django 4.1.7 on 2024-02-04 08:38

import business.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='citiz_back_image',
            field=models.ImageField(upload_to=business.models.business_directory_path),
        ),
        migrations.AlterField(
            model_name='business',
            name='optional_docs1_image',
            field=models.ImageField(blank=True, null=True, upload_to=business.models.business_directory_path),
        ),
        migrations.AlterField(
            model_name='business',
            name='optional_docs2_image',
            field=models.ImageField(blank=True, null=True, upload_to=business.models.business_directory_path),
        ),
        migrations.AlterField(
            model_name='business',
            name='optional_docs3_image',
            field=models.ImageField(blank=True, null=True, upload_to=business.models.business_directory_path),
        ),
    ]
