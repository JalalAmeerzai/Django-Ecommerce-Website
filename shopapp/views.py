from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
import json

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

    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shopapp/tracker.html')




def search(request):
    return render(request, 'shopapp/search.html')




def products(request, myid):
    #fetch the product using id
    prodView = Product.objects.filter(id=myid)
    params = {'product': prodView[0]}
    return render(request, 'shopapp/products.html', params)




def checkout(request):
    Message=""
    id = None
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Order(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        if items_json =='':
            Message = 0
        else:
            order.save()
            update = OrderUpdate(order_id=order.order_id, update_desc="Your order has been placed")
            update.save()
            Message = 1
            id = order.order_id

        return render(request, 'shopapp/checkout.html', {'id': id, "Message": Message})
    return render(request, 'shopapp/checkout.html')