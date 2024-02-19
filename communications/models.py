from django.db import models
from user.models import User

class Suggestions(models.Model):
    by = models.ForeignKey(User, related_name="suggested_by", on_delete = models.CASCADE, verbose_name= "Suggested by")
    description = models.TextField()
    datetime = models.DateTimeField(auto_now = True)

class Message(models.Model):
    to = models.ForeignKey(User,
            related_name='message_to',
            on_delete=models.CASCADE)
    user = models.ForeignKey(User,
            related_name='message_from',
            on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    message = models.TextField(null=True)
    image = models.ImageField(upload_to="messages_image/",null=True)
    
    class Meta:
        ordering = ['-created']    
