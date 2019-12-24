from django.shortcuts import render, redirect

import random 
# import time 

def index(request):
    if request.method == 'GET':
        if 'gold' in request.session:
            pass
        request.session['gold'] = 0
    return render(request, 'main_app/ninja.html')

def process_money(request):
    money = { 'farm': random.randint(10,20),
            'cave': random.randint(5,10),
            'house': random.randint(2,5),
            'casino': random.uniform(-50,50), 
    }
    if request.method == "POST":
        gold = request.POST['building']
        if gold in money.keys():
           request.session['gold'] += money[gold]
        return redirect('/')
