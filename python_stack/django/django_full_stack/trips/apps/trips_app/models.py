from django.db import models
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, postData):
        error = {}
        first_name = postData['first_name']
        last_name = postData['last_name']

        if User.objects.filter(email=postData['email']):
            error['emaildupe'] = "User already has an account with that email address"
            return error
        if not((len(first_name) > 2 ) & str.isalpha(first_name)):
            error["first_name"] = "First name should be at least two alphabets"
        if not((len(last_name) >2 ) & str.isalpha(last_name)):
            error["last_name"] = "Last name should be at least two alphabets"

        if not EMAIL_REGEX.match(postData['email']):
            error['email'] = ("Email address is invalid!")

        if len(postData['password']) < 8:
            error['password'] = "Password too short"
        if (postData['password'])!= (postData['confirm_pass']):
            error["confirm_pass"] = "Passwords do not match"
        return error


class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.CharField(max_length = 55)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now = True)
    # updated_at = models.DateTimeField(auto_now_add = True)
    objects = UserManager()

class TripManager(models.Manager):
    def trip_validator(self, postData):
        errors = {}
        if len(postData['destination']) < 1:
            errors['destination'] = 'destination should be at least Two characters'
        if len(postData['plan']) < 1:
            errors['plan'] = 'plan should be at least five characters'
        if len(postData['end_date']) < 1:
            errors['end_date'] = 'date is required'
        if len(postData['start_date']) < 1:
            errors['start_date'] = 'date is required'
        return errors

class Trip(models.Model):
    destination = models.CharField(max_length = 45)
    start_date = models.DateField(auto_now_add=False)
    end_date = models.DateField(auto_now_add=False)
    plan = models.CharField(max_length = 45)
    planner = models.ForeignKey(User, related_name = 'planned_trips')
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    objects = TripManager()

