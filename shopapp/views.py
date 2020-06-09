from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'shopapp/index.html')

def about(request):
    return render(request, 'shopapp/index.html')

def contact(request):
    return render(request, 'shopapp/index.html')

def tracker(request):
    return render(request, 'shopapp/index.html')

def search(request):
    return render(request, 'shopapp/index.html')

def productView(request):
    return render(request, 'shopapp/index.html')

def checkout(request):
    return render(request, 'shopapp/index.html')