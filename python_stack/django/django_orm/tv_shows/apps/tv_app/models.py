from django.db import models

# Create your models here.
class Shows(models.Model):
    title = models.CharField(max_length = 255)
    network = models.CharField(max_length = 255)
    release_date = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    