from django.db import models
from django.contrib.postgres.fields import ArrayField
from user.models import User


class Business(models.Model):
    name = models.CharField(max_length=255)
    images = ArrayField(models.ImageField(upload_to='business_images/', blank=True), blank=True, null=True)
    description = models.TextField()
    is_verified = models.BooleanField(
    "verified",
    default=False,
    help_text="Designates whether this business is verified or not. "
            "Unverified users cannot receive payments and are not displayed as business users."
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = False, blank = False)

    def __str__(self):
        return f"{self.name}"

    





