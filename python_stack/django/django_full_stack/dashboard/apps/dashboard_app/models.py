from django.db import models
import re

class UserManager(models.Manager):
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
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class TripManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['destination']) < 3:
            errors['destination'] = 'destination should be at least Two characters'
        if len(postData['plan']) < 5:
            errors['last_name'] = 'plan should be at least five characters'
class Trip(models.Model):
    destination = models.CharField(max_length = 255)
    start_date = models.DateTimeField(auto_now_add=False)
    end_date = models.DateTimeField(auto_now_add=False)
    plan = models.TextField()
    planner = models.ForeignKey(User, related_name = 'planned_trips')
    objects = TripManager()