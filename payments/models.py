from django.db import models

from user.models import User

class Payment(models.Model):
    token = models.CharField(max_length= 255)
    transaction_id = models.CharField(max_length= 255)
    amount = models.IntegerField()
    receiver = models.ForeignKey(User, related_name = "receiver", on_delete= models.CASCADE, null = False)
    sender = models.ForeignKey(User, related_name = "sender", on_delete= models.CASCADE, null = False)
    remarks = models.TextField()
    payment_datetime= models.DateTimeField( auto_now_add=True)


