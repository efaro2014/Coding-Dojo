from django.shortcuts import render, redirect
from .models import * 
# from apps.message_app.models import *
from django.contrib import messages
import bcrypt
# Create your views here.

def index(request):
    return render(request, 'dashboard_app/dash.html')

def register(request):
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
        conf_pw = request.POST['confirm_pass']
        User.objects.create(first_name = fname, last_name = lname, email= email, password= pw_hash)
        return redirect('/')

def login(request):
    user = User.objects.filter(email = request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            request.session['logged_in'] = True 
            request.session['first_name'] = logged_user.first_name
            return redirect('/read')
        else:
            messages.error(request, "YOUR PW DIDN'T MATCH")
            return redirect('/')
    else:
        messages.error(request, "The email was not found")
        return redirect("/")


def read(request):
    if 'logged_in' in request.session:
        context = {
        'all_trips': Trip.objects.all()
    }
        return render( request, "dashboard_app/read.html")
    else:
        messages.error(request,"User not recognized")
        return redirect("/")
 
def logout(request): 
    request.session.clear()
    return redirect('/')

def trips(request):
    if request.method == "GET":
        return render(request, 'dashboard_app/trips.html')
    if request.method == "POST":
        errors = Trip.objects.basic_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            planner = User.objects.get(id = request.session['userid'])
            dest = request.POST['destination']
            plan = request.POST['plan']
            sdate = request.POST['start_date']
            edate = request.POST['end_date']
            Trip.objects.create(destination = dest, plan = plan, start_date= sdate, end_date= edate, planner = planner )
            return redirect('/trips')









