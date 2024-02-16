from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from news.models import News
from user.models import User



class Report(models.Model):
    user = models.ForeignKey(User, related_name='reports', on_delete=models.CASCADE, null= True)
    post = models.ForeignKey(News, related_name='reports', on_delete=models.CASCADE, null= True)
    reason = models.TextField(verbose_name="reason of report")
    by = models.ForeignKey(User, related_name='reported_by', on_delete=models.CASCADE, verbose_name="reported by")
    # warning = models.ForeignKey(Warnings, related_name='warning_id', on_delete=models.CASCADE, verbose_name="led to warning")
    reported_date = models.DateTimeField(auto_now=True)


# Signal receivers to update report count
@receiver(post_save, sender=Report)
@receiver(post_delete, sender=Report)
def update_user_report_count(sender, instance, **kwargs):
    instance.user.report_count = instance.user.reports.count()
    instance.user.save()

