from django.db import models

class users(models.Model):
    name = models.CharField(max_length = 45)
    house = models.CharField(max_length=45)
    pet = models.CharField(max_length=45)
    year = models.IntegerField()

