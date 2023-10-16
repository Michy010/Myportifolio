from django.shortcuts import render
from . models import PortfolioProject

# Create your views here.

def index (request):
    return render (request, 'portifolio/home.html')

def about (request):
    return render (request, 'portifolio/about.html')

def services (request):
    return render (request, 'portifolio/services.html')

def portfolio (request):
    projects = PortfolioProject.objects.all()
    return render (request, 'portifolio/potifolio.html', {'projects':projects})

def contacts (request):
    return render (request, 'portifolio/contacts.html')