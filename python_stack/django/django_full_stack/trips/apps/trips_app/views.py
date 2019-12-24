from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
# Create your views here.
import bcrypt
def index(request):
    return render(request, 'trips_app/register.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) >0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        pw = request.POST['password']
        pw_hash = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
        user = User.objects.create(first_name = fname, last_name = lname,
        email= email, password= pw_hash)
        request.session['user_id'] = user.id
        request.session['user_id'] = True
        request.session['first_name'] = user.first_name
        return redirect('/home')

def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), 
        logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            request.session['user_id'] = True
            request.session['first_name'] = logged_user.first_name
            return redirect('/home')
        else:
            messages.error(request, 'The password is invalid')
            return redirect('/')
    else:
        messages.error(request, "The email is doesn't exist")
        return redirect('/')

def success(request):
    if 'user_id' in request.session:
        context = {
        'all_trips': Trip.objects.all()
        }
        return render(request, 'trips_app/home.html', context)
    else:
        messages.error(request, 'The user is not recognized please login')
        return redirect('/')
def logout(request):
    request.session.clear()
    return redirect('/')

def createTrip(request):
    return render(request, 'trips_app/new.html')

def addTrip(request):
    errors = Trip.objects.trip_validator(request.POST)
    if len(errors) >0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/trips')
    else:
        planner = User.objects.get(id = request.session['user_id'])
        dest = request.POST['destination']
        plan = request.POST['plan']
        sdate = request.POST['start_date']
        edate = request.POST['end_date']
        Trip.objects.create(destination = dest, plan = plan, start_date= sdate, end_date= edate, planner = planner )
        return redirect('/home')

def tripDetails(request, trip_id):
    all_trips ={
    'trip' : Trip.objects.get(id = trip_id)
    }
    return render(request,'trips_app/tripdetails.html',all_trips)

def deleteTrip(request,trip_id):
    trip = Trip.objects.get(id = trip_id)
    trip.delete()
    return redirect('/home')


def editTrip(request, trip_id):
    if request.method == "GET":
        all_trips ={
        'trip' : Trip.objects.get(id = trip_id)
        }
        return render(request,'trips_app/edit.html',all_trips)
    if request.method == 'POST':
        errors = Trip.objects.trip_validator(request.POST)
        if len(errors) >0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/trips/edit/'+trip_id)
        
        else:
            trip = Trip.objects.get(id= trip_id)
            trip.destination = request.POST['destination']
            trip.plan = request.POST['plan']
            trip.start_date = request.POST['start_date']
            trip.end_date = request.POST['end_date']
            trip.save()
            return redirect('/home')
       
def cancel(request):
    return redirect('/home')