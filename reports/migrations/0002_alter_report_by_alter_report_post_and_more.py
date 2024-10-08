# Generated by Django 4.1.7 on 2024-03-03 03:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0002_news_report_count'),
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reported_by', to=settings.AUTH_USER_MODEL, verbose_name='Reported by'),
        ),
        migrations.AlterField(
            model_name='report',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='news_report', to='news.news', verbose_name='Reported News'),
        ),
        migrations.AlterField(
            model_name='report',
            name='reason',
            field=models.TextField(verbose_name='Reason of report'),
        ),
        migrations.AlterField(
            model_name='report',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_reports', to=settings.AUTH_USER_MODEL, verbose_name='Reported User'),
        ),
    ]
