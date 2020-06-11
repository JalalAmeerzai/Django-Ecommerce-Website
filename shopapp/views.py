from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

def index(request):
    #products = Product.objects.all() #This will fetch all the products
    #n = len(products)
    #nSlides = n//4 + ceil((n/4)-(n//4))
    #params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'products': products}
    
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'shopapp/index.html', params)

def about(request):
    return render(request, 'shopapp/about.html')

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