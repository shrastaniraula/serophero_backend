# from django import apps
# from django.apps import apps
from django.utils.functional import cached_property
from django.utils.html import format_html
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, PermissionsMixin
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.db import models
# from business.models import Business

def user_image_path(instance, filename):
    phone_no = instance.phone_no
    filename = str(filename).split('.')[-1]
    return f'user_images/{phone_no}.{filename}'


class User(AbstractUser, PermissionsMixin):
    # Common fields
    email = models.EmailField(unique=True)
    username = models.CharField(unique=False, null=True,blank=True,max_length=50)
    phone_no = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to= user_image_path, null= True, blank= True)

    # User type choices
    USER_TYPE_CHOICES = (
        ('normal', 'Normal User'),
        ('business', 'Business User'),
        ('authority', 'Authority User'),
    )

    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='normal')

    # Fields specific to certain user types
    authority_role = models.CharField(max_length=255, null=True, blank=True)

    # Additional fields
    report_count = models.IntegerField(default=0)
    blacklisted = models.BooleanField(default=False)


    # image field

    REQUIRED_FIELDS=['phone_no', 'first_name', 'last_name']

    def update_report_count(self):
        self.report_count = self.report.count()
        self.save()

    def __str__(self):
        return f"{self.username}"
    
    @cached_property
    def display_image(self):
        html = '<a href="{img}"><img src="{img}" style="height:100px;">'
        if self.image:
            return format_html(html, img=self.image.url)
        return format_html('<strong>There is no image for this entry.<strong>')
    display_image.short_description = 'User image'
    


class Report(models.Model):
    user = models.ForeignKey(User, related_name='reports', on_delete=models.CASCADE, null= True)
    # post = models.ForeignKey(News, related_name='reports', on_delete=models.CASCADE, null= True)
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


