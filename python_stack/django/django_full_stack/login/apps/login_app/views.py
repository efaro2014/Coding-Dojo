from django.shortcuts import render, redirect
from .models import * 
from django.contrib import messages
import bcrypt
# Create your views here.

def index(request):
    return redirect('/create') 

def create(request):
    if request.method =='GET':
        return render(request, 'login_app/register.html')
    if request.method == 'POST':
        errors = Registration.objects.basic_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/create')
        else:
            fname = request.POST['first_name']
            lname = request.POST['last_name']
            email = request.POST['email']
            pw = request.POST['password']
            pw_hash = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
            print(pw_hash)
            conf_pw = request.POST['confirm_pass']
            Registration.objects.create(first_name = fname, last_name = lname, email= email, password= pw_hash, confirm_pass = conf_pw)
            return redirect('/create/read')

def login(request):
    user = Registration.objects.filter(email = request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id 
            return redirect('/create/success')
        else:
            messages.error(request, "YOUR PW DIDN'T MATCH")
            return redirect('/create')

def success(request):
    return render(request, 'login_app/success.html')

def clear(request):
    request.session.clear()
    return redirect('/create')

def read(request):
    context = {
    'all_shows': Registration.objects.all()
    }
    return render(request, 'login_app/read.html', context)