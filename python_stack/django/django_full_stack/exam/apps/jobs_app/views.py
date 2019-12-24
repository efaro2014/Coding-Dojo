from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
# Create your views here.
import bcrypt
def index(request):
    return render(request, 'jobs_app/register.html')

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
        # request.session['user_id'] = True
        request.session['first_name'] = user.first_name
        return redirect('/home')

def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), 
        logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            # request.session['user_id'] = True
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
        'all_jobs': Job.objects.all()
        }
        return render(request, 'jobs_app/home.html', context)
    else:
        messages.error(request, 'The user is not recognized please login')
        return redirect('/')
def logout(request):
    request.session.clear()
    return redirect('/')

def createJob(request):
    return render(request, 'jobs_app/new.html')

def addJob(request):
    errors = Job.objects.job_validator(request.POST)
    if len(errors) >0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/jobs')
    else:
        user = User.objects.get(id = request.session['user_id'])
        title = request.POST['title']
        location = request.POST['location']
        Job.objects.create(title = title, location = location, user = user )
        return redirect('/home')

def jobDetails(request, job_id):
    all_jobs ={
    'job' : Job.objects.get(id = job_id)
    }
    return render(request,'jobs_app/jobdetails.html', all_jobs)

def deleteJob(request, job_id):
    if 'user_id' in request.session:
        job = Job.objects.get(id = job_id)
        job.delete()
        return redirect('/home')

def editJob(request, job_id):
    if request.method =='GET':
        all_jobs ={
            'job' : Job.objects.get(id = job_id)
            }
        return render(request,'jobs_app/edit.html', all_jobs)
    if request.method =='POST':
        errors = Job.objects.job_validator(request.POST)
        if len(errors) >0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/jobs/edit/'+job_id)
        else:
            job = Job.objects.get(id= job_id)
            job.title = request.POST['title']
            job.description  = request.POST['description']
            job.location = request.POST['location']
            job.save()
            return redirect('/home')

def cancel(request):
    return redirect('/home')


    