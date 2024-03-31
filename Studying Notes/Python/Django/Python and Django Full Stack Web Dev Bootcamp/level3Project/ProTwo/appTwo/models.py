from django.db import models

# Create your models here.
class UserSignup(models.Model):
    username = models.CharField(max_length=128,unique=True)
    userpass = models.CharField(max_length=128,unique=True)
    useremail = models.EmailField(max_length=254,unique=True)
