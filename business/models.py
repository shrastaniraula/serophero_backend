from django.db import models
from django.contrib.postgres.fields import ArrayField
from user.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone


def business_directory_path(instance, filename):
    return f'business_images/{instance.name}/{filename}'

class Business(models.Model):
    name = models.CharField(max_length=255)
    citiz_front_image = models.ImageField(upload_to= business_directory_path, verbose_name="Citizenship photo front")
    citiz_back_image = models.ImageField(upload_to= business_directory_path, verbose_name="Citizenship photo back")
    optional_docs1_image = models.ImageField(upload_to= business_directory_path, null= True, blank= True, verbose_name="Additional verifying photo 1")
    optional_docs2_image = models.ImageField(upload_to= business_directory_path, null= True, blank= True, verbose_name="Additional verifying photo 2")
    optional_docs3_image = models.ImageField(upload_to= business_directory_path, null= True, blank= True, verbose_name="Additional verifying photo 3")

    description = models.TextField()
    is_verified = models.BooleanField(
    "verified",
    default=False,
    help_text="Designates whether this business is verified or not. "
            "Unverified users cannot receive payments and are not displayed as business users."
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = False, blank = False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name}"
    
@receiver(post_save, sender=Business)
def update_user_type(sender, instance, created, **kwargs):
    if not created:
        user = instance.user
        if instance.is_verified:
            user.user_type = 'business'
            user.save()








