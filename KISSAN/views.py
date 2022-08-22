from django.shortcuts import render
from KISSAN.models import crops
from math import ceil

# Create your views here.
def home(request) :
    return render(request, 'home.html')

def index(request) :
    Crops = crops.objects.all()
    n = len(Crops)
    nslides = n//3 + ceil((n/3)-(n//3))
    params = {'no_of_slides':nslides ,'crop':Crops}
    return render(request, 'index.html', params)

def analyse(request) :
    Crops = crops.objects.all()
    n = len(Crops)
    params = {'no_of_slides':n,'crop':Crops}
    return render(request, 'analysis.html', params)

def Predict(request) :
    return render(request, 'prediction.html')