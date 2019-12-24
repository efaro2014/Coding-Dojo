from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def index(request):
    # context = {
    #     'all_shows': Shows.objects.all()
    # }
    if request.method == 'GET':
        return render(request, 'tv_app/create.html') 
    if request.method == "POST":
        title = request.POST['title']
        network = request.POST['network']
        date = request.POST['release_date']
        desc = request.POST['description']
        Shows.objects.create(title = title, network = network, release_date= date, description= desc)
        return redirect('/')
def read(request):
    context = {
    'all_shows': Shows.objects.all()
    }
    return render(request, 'tv_app/read.html', context) 

def read_one(request, shows_id):
    all_shows = {
    'show' : Shows.objects.get(id = shows_id)
    }
    return render(request,'tv_app/read_one.html',all_shows)

def delete_show(request, shows_id):
    show = Shows.objects.get(id = shows_id)
    show.delete()
    return redirect('/read')

def edit_show(request, shows_id):
    if request.method == "GET":
        all_shows = {
        'show' : Shows.objects.get(id = shows_id)
        }
        return render(request, 'tv_app/edit.html', all_shows)
    if request.method == 'POST':
        show = Shows.objects.get(id = shows_id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.desc = request.POST['description']
        show.save()
        return redirect('/read/'+shows_id)



    
