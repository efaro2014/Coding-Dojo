from django.shortcuts import render, redirect
from .models import * 
from django.contrib import messages
from apps.login_app.models import *
import bcrypt

# Create your views here.
def index(request):
    context = {
        'all_messages': Message.objects.all(),
        
    }
    return render(request, 'message_app/messages.html', context)

def create_msg(request):
    if request.method == 'POST':
        msg = request.POST['message']
        user = Registration.objects.get(id = request.session['userid'])
        Message.objects.create(msg_text = msg, user = user)
        return redirect('/wall')

def create_cmt(request):
    cmt = request.POST['comments']
    user = Registration.objects.get(id = request.session['userid'])
    # if msg: 
    msg = Message.objects.get(id = request.POST['message_id'])
    Comments.objects.create(cmt_text = cmt, messages = msg, user= user )
    return redirect('/wall')

def delete_cmt(request):
    user = Registration.objects.get(id = request.session['userid'])
    cmt = Comments.objects.get(id = request.POST['destroy'])
    cmt.delete()
    return redirect('/wall')
