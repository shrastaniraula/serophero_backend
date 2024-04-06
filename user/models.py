from django.utils.functional import cached_property
from django.utils.html import format_html
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


def user_image_path(instance, filename):
    phone_no = instance.phone_no
    filename = str(filename).split('.')[-1]
    return f'user_images/{phone_no}.{filename}'


class User(AbstractUser, PermissionsMixin):
    # Common fields
    email = models.EmailField(unique=True)
    username = models.CharField(unique=False, null=True,blank=True,max_length=50)
    phone_no = models.CharField(max_length=15, unique=True, null= True, blank= True)
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


    # REQUIRED_FIELDS=['phone_no', 'first_name', 'last_name']


    def __str__(self):
        return f"{self.email}"
    
    @cached_property
    def display_image(self):
        html = '<a href="{img}"><img src="{img}" style="height:100px;">'
        if self.image:
            return format_html(html, img=self.image.url)
        return format_html('<strong>There is no image for this entry.<strong>')
    display_image.short_description = 'User image'
    

class MobileTokens(models.Model):
    phone_key = models.CharField(max_length = 255)
    device_name = models.CharField(max_length = 255)
    user = models.ForeignKey(User, related_name = 'user', on_delete = models.CASCADE)
    is_logged_in = models.BooleanField( "logged in", default=True)
