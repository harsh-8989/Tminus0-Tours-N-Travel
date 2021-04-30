from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'developer/index.html'),


def print(request):
    return render(request, 'developer/print.html')
