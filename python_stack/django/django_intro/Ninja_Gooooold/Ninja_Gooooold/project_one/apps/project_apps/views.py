from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    if request.method == "GET":
        if 'bank' not in request.session:
            request.session['bank']= 25
    return render(request,"project_apps/index.html")

def route(request):
    if request.method == "POST":
        if request.POST['location'] == 'farm':
            request.session['bank'] += random.randint(10,20)

        elif request.POST['location'] == 'cave':
            request.session['bank'] += random.randint(5,10)

        elif request.POST['location'] == 'house':
            request.session['bank'] += random.randint(2,5)

        elif request.POST['location'] == 'casino':
            request.session['bank'] += random.randint(-50,50)

        return redirect('/')