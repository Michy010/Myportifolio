from django.shortcuts import render

# Create your views here.

def index (request):
    return render (request, 'portifolio/home.html')

def about (request):
    return render (request, 'portifolio/about.html')

def services (request):
    return render (request, 'portifolio/services.html')

def portfolio (request):
    return render (request, 'portifolio/potifolio.html')

def contacts (request):
    return render (request, 'portifolio/contacts.html')