# from __future__ import unicode_literals
from django.db import models


class ShowsManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = 'Title should be at least Two characters'
        if len(postData['network']) < 3:
            errors['netwrok'] = 'Netwrok should be at least three characters'
        if len(postData['release_date']) <6:
            errors['release_date'] = 'The date given is not valid'
        if len(postData['description']) and len(postData['description']) !=0:
            errors['description'] = 'This is not valid description'
        return errors
# Create your models here.
class Shows(models.Model):
    title = models.CharField(max_length = 255)
    network = models.CharField(max_length = 255)
    release_date = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    objects = ShowsManager()