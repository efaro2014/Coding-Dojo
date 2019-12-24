from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def index(request):
    if request.method =="GET":
        return render(request, 'user_app/index.html')
    if request.method == 'POST':
        name = request.POST['full_name']
        email = request.POST['email']
        age = request.POST['age']
        User.objects.create(full_name = name, email = email, age = age)
        return redirect('/')
