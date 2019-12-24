from django.db import models
import re
import bcrypt
email_regex =  re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
     

# Create your models here.
# class UserManager(models.Manager):
#     def basic_validator(self, postData):
#         errors = {}
#         if len(postData['first_name']) < 2:
#             errors['first_name'] = 'First name should be at least Two characters'
#         if len(postData['last_name']) < 2:
#             errors['last_name'] = 'First name should be at least Two characters'
#         if not email_regex.match(postData['email']):
#             errors['email'] = 'Invalid email address!'
#         if User.objects.filter(email = postData['email']):
#             postData['emaildope'] = 'The email already exists'
#         if len(postData['password']) <5:
#             errors['password'] = 'The password given is not valid'
#         if (postData['password']) != (postData['confirm_pass']):
#             errors['confirm_pass'] = 'The password doesn\'t match the password input'
#         return errors

class UserManager(models.Manager):
    def basic_validator(self, postData):
        error = {}

        first_name = postData['first_name']
        last_name = postData['last_name']

        if User.objects.filter(email=postData['email']):
            error['emaildupe'] = "User already has an account with that email address"
            return error
        if not((len(first_name) >2 ) & str.isalpha(first_name)):
            error["first_name"] = "First name should be populated"
        if not((len(last_name) >2 ) & str.isalpha(last_name)):
            error["last_name"] = "Last name should be populated"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            error['email'] = ("Email address is invalid!")

        if len(postData['password']) < 8:
            error['password'] = "Password too short"
        if (postData['password'])!= (postData['pw_confirm']):
            error["pw_confirm"] = "Passwords do not match"

        return error

   

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # liked_books = models.ForeignKey(Book, related_name= 'users')
    # books_uploaded = models.ForeignKey(Book, related_name='users')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    objects = UserManager()

class BookManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # email_regex =  re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['title']) == None:
            errors['title'] = 'Title is required!'
        if len(postData['description']) < 5:
            errors['description'] = 'Description should be at least 5 characters'  

class Book(models.Model):
    title = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(User, related_name='books_uploaded')
    users_who_like = models.ForeignKey(User, related_name = 'liked_books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField()
    objects = BookManager()