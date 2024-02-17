from django.db import models
from user.models import User

class Suggestions(models.Model):
    by = models.ForeignKey(User, related_name="suggested_by", on_delete = models.CASCADE, verbose_name= "Suggested by")
    description = models.TextField()
    datetime = models.DateTimeField(auto_now = True)
    #to?
    
