from accounts.decorators import unauthenticated_user
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users, unauthenticated_user, admin_only
from django.contrib.auth.models import Group

# Create your views here.
@login_required(login_url='login')
@admin_only
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    product = Product.objects.all()
    return render(request, 'accounts/products.html',{'products':product})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customers(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    orders_count = orders.count()

    myfilter = OrderFilter(request.GET,queryset=orders)
    orders = myfilter.qs

    context = {'customer':customer,'orders':orders, 'orders_count':orders_count, 'myfilter':myfilter}
    return render(request, 'accounts/customer.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_orders(request, pk):
    orders = order.objects.get(id=pk)
    if request.method == 'POST':
        orders.delete()
        return redirect('/')
    context = {'item':orders}
    return render(request, 'accounts/delete.html', context)

@unauthenticated_user
def register_page(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            messages.success(request, 'Account has been successfully created for '+ username)
            return redirect('login')
    context ={'form':form}
    return render(request, 'accounts/register.html', context)

@unauthenticated_user
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.info(request, 'Username Or Password is incorrect')

    context ={}
    return render(request, 'accounts/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')

def user_page(request):
    context = {}
    return render(request, 'accounts/user.html', context)