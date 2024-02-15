from django.db import models
from user.models import User

class News(models.Model):
    author = models.ForeignKey(User, related_name = "author", on_delete= models.CASCADE, null = False)
    news_heading = models.CharField(max_length= 255)
    news_description = models.TextField()
    news_image = models.ImageField(upload_to= "news_images/", verbose_name="News thumbnail")
    post_date= models.DateField( auto_now=True)
    is_verified = models.BooleanField(
    "verified",
    default=False,
    )

