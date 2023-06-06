from django.db import models

# Create your models here.
class profile(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=200)
    phone_number=models.CharField(max_length=10)
    Qualification=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
