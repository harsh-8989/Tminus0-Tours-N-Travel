from django.shortcuts import render

# Create your views here.
from ToursNTravels.models import *


def index(request):
    return render(request, 'developer/index.html'),


def print(request):
    purchase_ = purchase.objects.all()
    return render(request, 'developer/print.html', {'transtions': purchase_})
