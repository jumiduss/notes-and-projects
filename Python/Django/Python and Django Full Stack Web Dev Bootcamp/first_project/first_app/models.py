from django.db import models

class User(models.Model):
    fname = models.CharField(max_length = 264, unique=True)
    lname = models.CharField(max_length = 264, unique=True)
    email = models.CharField(max_length = 264, unique=True)

    def __str__(self):
        return self.lname