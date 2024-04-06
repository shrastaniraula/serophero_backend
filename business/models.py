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
            sendnotification()
            user.save()




import json

import requests


def sendnotification(): 
            print("Devices")
            url = "https://fcm.googleapis.com/fcm/send"
            # topic = f"YOUR_TOPIC_NAME{topic_id}"
            data = {
                  
                  "notification": 
                        {
                              "title": "Business Verified", 
                              "body": "Your business has been verified", 
                              "mutable_content": True,
                        },
                  "registration_ids": ['cWxoWp4URImZotBwCXqBqT:APA91bHYtQxOnrpJdr9e1I8ve23Z6I1YiNvLprShBEx4uWp7x_PX1wCML6Wp8urM8FtD84SvI7DM-BfC4chUXyBjUlLFe9tTppbGEudsMmg3da95PVUIpQBjagwExTeNjZx4SWQKkZRT'],
            }

            headers = {"Content-Type": "application/json", "Authorization": "key=AAAArq22cEQ:APA91bE9pVyI0mhPO_zfJbk4CmgeRxgJorAyGbv-MK1_n9TqoyIuM9PgpuluPh2HgE2bggEkfhcwx1tTFpEx6UmE3mVGkRtm3fijVgdo0SdyZN-o0yEqLtBiHytQIEcDYh4j-9rXRk4P"}
            payload = json.dumps(data, default=int)
            print("Payload")
            print(payload)
            response = requests.post(url, headers=headers, data=payload)
            print("Successfully sent notification:", response.status_code)

            # return requests.Response({'data':response.content})









