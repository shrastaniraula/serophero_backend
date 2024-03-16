from django.db import models
from user.models import User

class Suggestions(models.Model):
    by = models.ForeignKey(User, related_name="suggested_by", on_delete = models.CASCADE, verbose_name= "Suggested by")
    description = models.TextField()
    datetime = models.DateTimeField(auto_now = True)

class Message(models.Model):
    receiver = models.ForeignKey(User,
            related_name='sent_messages',
            on_delete=models.CASCADE)
    sender = models.ForeignKey(User,
            related_name='received_messages',
            on_delete=models.CASCADE,)
    created = models.DateTimeField(auto_now_add=True)
    message = models.TextField(null=True)
    image = models.ImageField(upload_to="messages_image/",null=True, blank=True)
    
    class Meta:
        ordering = ['-created']    
