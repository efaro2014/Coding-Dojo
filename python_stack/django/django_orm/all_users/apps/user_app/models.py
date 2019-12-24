from django.db import models

# Create your models here.
class user(models.Model):
    full_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    age = models.IntegerField()