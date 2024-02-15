# Generated by Django 4.1.7 on 2024-02-05 13:08

import business.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_alter_business_citiz_back_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='citiz_back_image',
            field=models.ImageField(upload_to=business.models.business_directory_path, verbose_name='Citizenship photo back'),
        ),
        migrations.AlterField(
            model_name='business',
            name='citiz_front_image',
            field=models.ImageField(upload_to=business.models.business_directory_path, verbose_name='Citizenship photo front'),
        ),
        migrations.AlterField(
            model_name='business',
            name='optional_docs1_image',
            field=models.ImageField(blank=True, null=True, upload_to=business.models.business_directory_path, verbose_name='Additional verifying photo 1'),
        ),
        migrations.AlterField(
            model_name='business',
            name='optional_docs2_image',
            field=models.ImageField(blank=True, null=True, upload_to=business.models.business_directory_path, verbose_name='Additional verifying photo 2'),
        ),
        migrations.AlterField(
            model_name='business',
            name='optional_docs3_image',
            field=models.ImageField(blank=True, null=True, upload_to=business.models.business_directory_path, verbose_name='Additional verifying photo 3'),
        ),
    ]