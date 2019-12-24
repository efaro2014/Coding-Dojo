from django.shortcuts import render, redirect
from .models import * 
from django.contrib import messages
import bcrypt
import re
email_regex =  re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    
# Create your views here.
def index(request):
    if request.method =='GET':
        return render(request, 'books/books.html')
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            fname = request.POST['first_name']
            lname = request.POST['last_name']
            email = request.POST['email']
            pw = request.POST['password']
            pw_hash = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
            print(pw_hash)
            # conf_pw = request.POST['confirm_pass']
            User.objects.create(first_name = fname, last_name = lname, email= email, password= pw_hash)
            request.session['user_id'] = user.id
            request.session['user_id'] = True
            return redirect('/books')

def login(request):
    user = User.objects.filter(email= request.POST['email']) 
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            # request.session['user_id'] = User.objects.get(email = request.POST['email']).id
            request.session['logged_in'] = True
            request.session['first_name'] = logged_user.first_name
            return redirect('/books')
        else:
            messages.error(request, "Password is not correct")
            return redirect("/")

    messages.error(request, "The email was not found")
    return redirect("/")






