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
    updated_at = models.DateTimeField(auto_now_add = True)
    objects = UserManager()

class JobManager(models.Manager):
    def job_validator(self, postData):
        errors = {}
        if len(postData['title']) < 3:
            errors['title'] = 'Job title should be at least three characters'
        if len(postData['location']) < 1:
            errors['location'] = 'location is required'
        return errors
class Job(models.Model):
    title = models.CharField(max_length = 45)
    location = models.CharField(max_length = 45)
    description = models.TextField()
    user = models.ForeignKey(User, related_name = 'jobs_list')
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    objects = JobManager()