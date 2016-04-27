from django.db import models

# Create your models here.
class User_Info(models.Model):
    user=models.CharField(max_length=20)
    password=models.CharField(max_length=32)
    email=models.EmailField(max_length=32)
    mobile=models.IntegerField(max_length=12)
    role=models.IntegerField(max_length=3)