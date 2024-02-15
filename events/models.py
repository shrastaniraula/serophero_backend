from django.utils.timezone import datetime
from django.db import models
from django.contrib.postgres.fields import ArrayField
from user.models import User

class Event(models.Model):
    by = models.ForeignKey(User, related_name='by', on_delete=models.CASCADE, null= False)
    title = models.CharField(max_length= 255)
    description = models.TextField()
    location = models.CharField(max_length= 100)
    post_date= models.DateField( auto_now=True)
    event_date= models.DateField( auto_now=False, default= datetime.now())
    event_image = models.ImageField(upload_to= "events_images/", verbose_name="Event thumbnail")
    allowed_members = models.ManyToManyField(User, related_name='allowed_events')

