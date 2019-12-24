from django.shortcuts import render
from time import gmtime, strftime
# Create your views here.
def index(request):
    time_zones = { 
        'time': strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request, 'main_app/index.html', time_zones)