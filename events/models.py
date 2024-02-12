from django.db import models


class Business(models.Model):
    name = models.CharField(max_length=255)
    citiz_front_image = models.ImageField(upload_to= business_directory_path, verbose_name="Citizenship photo front")
    citiz_back_image = models.ImageField(upload_to= business_directory_path, verbose_name="Citizenship photo back")
    optional_docs1_image = models.ImageField(upload_to= business_directory_path, null= True, blank= True, verbose_name="Additional verifying photo 1")
    optional_docs2_image = models.ImageField(upload_to= business_directory_path, null= True, blank= True, verbose_name="Additional verifying photo 2")
    optional_docs3_image = models.ImageField(upload_to= business_directory_path, null= True, blank= True, verbose_name="Additional verifying photo 3")
