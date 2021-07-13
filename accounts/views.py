from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import *
from .filters import OrderFilter

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

    myfilter = OrderFilter(request.GET,queryset=orders)
    orders = myfilter.qs

    context = {'customer':customer,'orders':orders, 'orders_count':orders_count, 'myfilter':myfilter}
    return render(request, 'accounts/customer.html', context)

def create_orders(request, pk):
    orderformset = inlineformset_factory(Customer, order, fields=('product','status'), extra=5)
    customer = Customer.objects.get(id=pk)
    formset = orderformset(queryset=order.objects.none(),instance=customer)
    if request.method == 'POST':
        formset = orderformset(request.POST,instance = customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context={'formset':formset}
    return render(request, 'accounts/order_form.html', context)

def update_orders(request, pk):
    orders = order.objects.get(id=pk)
    form = OrderForm(instance=orders)
    if request.method == 'POST':
        form = OrderForm(request.POST,instance=orders)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)

def delete_orders(request, pk):
    orders = order.objects.get(id=pk)
    if request.method == 'POST':
        orders.delete()
        return redirect('/')
    context = {'item':orders}
    return render(request, 'accounts/delete.html', context)