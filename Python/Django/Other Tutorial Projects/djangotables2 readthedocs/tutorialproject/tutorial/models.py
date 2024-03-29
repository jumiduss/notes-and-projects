from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    user = models.ForeignKey(get_user_model(),null=True, on_delete=models.CASCADE)
    birth_date = models.DateField()
