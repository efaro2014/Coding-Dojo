from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse('I did it!')

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/new')

def method(request, my_val):
    return  HttpResponse(f"placeholder to display blog number: {my_val }")

def destroy(request, my_val):
    return redirect('/')