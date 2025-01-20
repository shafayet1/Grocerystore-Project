from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages
import requests

# Create your views here.

def get_weather_data():
    api_key = 'cc166ef7df4fd6e63cee327a5690c158'
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q=Toronto&units=metric&appid={api_key}"
    )
    if weather_data.status_code == 200:
        weather_json = weather_data.json()
        if weather_json.get('cod') == 404:
            return None, None
        else:
            weather = weather_json['weather'][0]['main']
            temp = round(weather_json['main']['temp'])
            return weather, temp
    else:
        return None, None

@login_required
def index(request):
    weather, temp = get_weather_data()
    
    orders = Order.objects.all()
    products = Product.objects.all()
    orders_count = orders.count()
    product_count = products.count()
    workers_count = User.objects.all().count()
    if request.method =='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm() 
    context = {
        'orders': orders,
        'form' : form,
        'products' : products,
        'workers_count' : workers_count,
        'orders_count' : orders_count,
        'product_count' : product_count,
        'weather' : weather,
        'temp' : temp,
    }
    return render(request, 'dashboard/index.html', context)
    #return HttpResponse('<h1 style="color: DodgerBlue;"> This is the Index Page </h1>')

@login_required
def staff(request):
    workers = User.objects.all()
    workers_count = workers.count()
    orders_count = Order.objects.all().count
    product_count = Product.objects.all().count
    context = {
        'workers' : workers,
        'workers_count' : workers_count,
        'orders_count' : orders_count,
        'product_count' : product_count,
    }
    return render(request, 'dashboard/staff.html', context)
    #return HttpResponse('Staff page')

@login_required
def staff_detail(request, pk):
    workers = User.objects.get(id=pk)
    context = {
        'workers' : workers,
    }
    return render(request, 'dashboard/staff_detail.html', context)
    #return HttpResponse('Staff page')

@login_required
def product(request):
    items = Product.objects.all()
    product_count = items.count
    workers_count = User.objects.all().count
    orders_count = Order.objects.all().count
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid:
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-product')
    else:
        form = ProductForm
    context={
        'items' : items,
        'form' : form,
        'workers_count' : workers_count,
        'orders_count' : orders_count,
        'product_count' : product_count,

    }
    return render(request, 'dashboard/product.html', context)

@login_required
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    
    return render(request, 'dashboard/product_delete.html')

@login_required
def product_edit(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/product_edit.html', context)

@login_required
def order(request):
    orders = Order.objects.all()
    orders_count = orders.count()
    workers_count = User.objects.all().count
    product_count = Product.objects.all().count

    context={
        'orders' : orders,
        'workers_count' : workers_count,
        'orders_count' : orders_count,
        'product_count' : product_count,
    }
    return render(request, 'dashboard/order.html', context)
