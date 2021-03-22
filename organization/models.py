from django.db import models


# Create your models here.
class Problem(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    von = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    subject = models.CharField(max_length=150)
    detailproblem = models.CharField(max_length=1000)
    status = models.CharField(max_length=100,default=0)