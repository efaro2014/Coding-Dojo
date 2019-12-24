from django.db import models
import re
from apps.login_app.models import Registration

# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(Registration, related_name='messages')
    msg_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comments(models.Model):
    user = models.ForeignKey(Registration, related_name= 'comments')
    cmt_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    messages = models.ForeignKey(Message, related_name = 'comments')

