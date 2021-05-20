from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import *


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')

def store(request):
    product = Product.objects.all()
    return render(request, 'store.html', {"product" : product})


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order ,created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
    context={'items':items}
    return render(request, 'cart.html',context)


def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc, date=datetime.today())
        contact.save()
        
    return render(request, 'contact.html')

# Create your views here.
