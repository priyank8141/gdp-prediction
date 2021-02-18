from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class appusers(models.Model):
    mobile = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    role = models.CharField(max_length=50, blank=True)
    von = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=100, blank=True)
    district = models.CharField(max_length=100, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
