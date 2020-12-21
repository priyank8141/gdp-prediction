
from django.db import models


# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    role = models.CharField(max_length=50)
    von = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    password = models.CharField(max_length=150)





