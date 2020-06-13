from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact
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
    params={"Message": -1}
    if request.method == 'POST':
        name = request.POST.get("name", None)
        email = request.POST.get("email", None)
        phone = request.POST.get("phone", None)
        desc = request.POST.get("desc", None)

        message = Contact(sender_name = name, sender_email = email, sender_phone =  phone, msg_desc = desc)
        try:
            message.save()
            params["Message"] = 1
        except Exception as identifier:
            params["Message"] = 0
    return render(request, 'shopapp/contact.html',params)




def tracker(request):
    return render(request, 'shopapp/tracker.html')




def search(request):
    return render(request, 'shopapp/search.html')




def products(request, myid):
    #fetch the product using id
    prodView = Product.objects.filter(id=myid)
    params = {'product': prodView[0]}
    return render(request, 'shopapp/products.html', params)




def checkout(request):
    return render(request, 'shopapp/checkout.html')