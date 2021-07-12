from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    orders = order.objects.all()
    customers  = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'orders':orders, 
        'customers':customers,
        'total_orders':total_orders,
        'delivered':delivered,
        'pending':pending,
        }

    return render(request, 'accounts/dashboard.html', context)

def products(request):
    product = Product.objects.all()
    return render(request, 'accounts/products.html',{'products':product})

def customers(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    orders_count = orders.count()
    context = {'customer':customer,'orders':orders, 'orders_count':orders_count}
    return render(request, 'accounts/customer.html', context)