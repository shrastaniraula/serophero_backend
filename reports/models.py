from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from news.models import News
from user.models import User

class Warning(models.Model):
    warning_date = models.DateTimeField(auto_now=True)
    message = models.TextField()
    user_warned = models.ForeignKey(User, related_name='warning', on_delete=models.CASCADE, null= True)
    # is_blacklisted = models.BooleanField()

class Blacklist(models.Model):
    user = models.ForeignKey(User, related_name = 'blacklist', on_delete = models.CASCADE)
    blacklisted_date = models.DateTimeField(auto_now=True)



class Report(models.Model):
    user = models.ForeignKey(User, related_name='user_reports', on_delete=models.CASCADE, null= True, blank = True, verbose_name="Reported User")
    post = models.ForeignKey(News, related_name='news_report', on_delete=models.CASCADE, null= True, blank = True, verbose_name="Reported News")
    reason = models.TextField(verbose_name="Reason of report")
    by = models.ForeignKey(User, related_name='reported_by', on_delete=models.CASCADE, verbose_name="Reported by")
    # warning = models.ForeignKey(Warnings, related_name='warning_id', on_delete=models.CASCADE, verbose_name="led to warning")
    reported_date = models.DateTimeField(auto_now=True)


@receiver(post_save, sender=Report)
def update_report_count(sender, instance, created, **kwargs):
    if created:
        if instance.post is None and instance.user:
            user = instance.user
            user.report_count += 1
            user.save()

            print(user.report_count)

            # Check if a warning should be issued
            if user.report_count >= 5:
                # Create a warning
                Warning.objects.create(message="Exceeded report threshold", user_warned=user)

            # Check if blacklisting should occur
            if user.report_count >= 15:
                # Create a blacklist entry
                Blacklist.objects.create(user=user)

        if instance.user is None and instance.post:
            post = instance.post
            post.report_count += 1
            post.save()

            if post.report_count >= 15:
                post.is_verified = False
                post.save()





