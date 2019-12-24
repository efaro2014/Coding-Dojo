from django.db import models
import re

class RegistrationManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        email_regex =  re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First name should be at least Two characters'
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'First name should be at least Two characters'
        if not email_regex.match(postData['email']):
            errors['email'] = 'Invalid email address! '
        if len(postData['password']) <8:
            errors['password'] = 'The password given is not valid'
        if (postData['password']) != (postData['confirm_pass']):
            errors['confirm_pass'] = 'The password doesn\'t match the password input'
        return errors
# Create your models here.
class Registration(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    confirm_pass = models.CharField(max_length = 255)
    objects = RegistrationManager()