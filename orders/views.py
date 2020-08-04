from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import re
from .forms import SignUpForm
from datetime import date, datetime
import datetime as d

from .models import Item, Size, Topping, Subtopping, Order, Confirmed, Complete

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    context = {
        "user": request.user,
        "pasta": Item.objects.filter(item_category="Pasta"),
        "salad": Item.objects.filter(item_category="Salads"),
        'platter': Size.objects.filter(size_category="Dinner Platters"),
        "sub": Size.objects.filter(size_category="Subs"),
        "subtopping": Subtopping.objects.all(),
        "regular": Size.objects.filter(size_category="Regular Pizza"),
        "sicilian": Size.objects.filter(size_category="Sicilian Pizza"),
        "toppings": Topping.objects.all(),
    }
    return render(request, 'orders/index.html', context)

def add(request):
    try:
        item_id = request.POST['add-item']
        item = Item.objects.get(pk=item_id)
        today = date.today()
        timestamp = datetime.now().time()
        order = Order(order_date=today, order_time=timestamp, user=request.user.id, item_name=item.item_name, item_category=item.item_category, item_size="", item_toppings_num=0, item_toppings_list="", item_total_price=item.item_price)
    except KeyError:
        return render(request, 'orders/error.html')
    
    order.save()
    return redirect('index')

def addsize(request):
    try:
        data = request.POST['addsizeitem']
        print(f"data: {data}")
        data_list = data.split()
        item_id = data_list[0]
        item_size = data_list[1]
        item_price = data_list[2]
        item = Size.objects.get(pk=item_id)
        today = date.today()
        timestamp = datetime.now().time()
        order = Order(order_date=today, order_time=timestamp, user=request.user.id, item_name=item.size_name, item_category=item.size_category, item_size=item_size, item_toppings_num=0, item_toppings_list="", item_total_price=item_price)
    except KeyError:
        return render(request, 'orders/error.html')
    order.save()
    return redirect('index')

def addsizecheese(request):
    try:
        data = request.POST['addsizeitem']
        data_list = data.split()
        item_id = data_list[0]
        item_size = data_list[1]
        item_price = data_list[2]
        item = Size.objects.get(pk=item_id)
        today = date.today()
        timestamp = datetime.now().time()
        order = Order(order_date=today, order_time=timestamp, user=request.user.id, item_name=item.size_name, item_category=item.size_category, item_size=item_size, item_toppings_num=0, item_toppings_list="", item_total_price=item_price)
    except KeyError:
        data = request.POST['addsizeitemcheese']
        data_list = data.split()
        item_id = data_list[0]
        item_size = data_list[1]
        item_price = float(data_list[2]) + float(0.5)
        item = Size.objects.get(pk=item_id)
        today = date.today()
        timestamp = datetime.now().time()
        order = Order(order_date=today, order_time=timestamp, user=request.user.id, item_name=item.size_name, item_category=item.size_category, item_size=item_size, item_toppings_num=1, item_toppings_list="extra cheese", item_total_price=item_price)
    except KeyError:
        return render(request, 'orders/error.html')
    order.save()
    return redirect('index')

def addsizetop(request):
    try:
        data = request.POST['addsizeitem']
        print(f"data: {data}")
        data_list = data.split()
        print(f"data list: {data_list}")
        item_id = data_list[0]
        item_size = data_list[1]
        item_tops_num = data_list[2]
        item_toppings = " ".join(data_list[3:])
        item = Size.objects.get(pk=item_id)
        if item_size == 'small':
            item_price = float(item.size_small_price) + (float(item_tops_num) * float(0.5))
        elif item_size == 'large':
            item_price = float(item.size_large_price) + (float(item_tops_num) * float(0.5))
        today = date.today()
        timestamp = datetime.now().time()
        print(f"item: {item.size_name} num of tops: {item_tops_num} (toppings: {item_toppings}) item size: {item_size} item price: {item_price}")
        order = Order(order_date=today, order_time=timestamp, user=request.user.id, item_name=item.size_name, item_category=item.size_category, item_size=item_size, item_toppings_num=item_tops_num, item_toppings_list=item_toppings, item_total_price=item_price)
    except KeyError:
        return render(request, 'orders/error.html')
    order.save()
    return redirect('index')

def addsizepizza(request):
    try:
        data = request.POST['addsizeitem']
        print(f"data: {data}")
        data_list = data.split()
        print(f"data list: {data_list}")
        item_id = data_list[0]
        item_size = data_list[1]
        item_tops_num = data_list[2]
        item_toppings = " ".join(data_list[3:])
        item = Size.objects.get(pk=item_id)
        if item_size == 'small':
            item_price = item.size_small_price
        elif item_size == 'large':
            item_price = item.size_large_price
        today = date.today()
        timestamp = datetime.now().time()
        print(f"item: {item.size_name} num of tops: {item_tops_num} (toppings: {item_toppings}) item size: {item_size} item price: {item_price}")
        order = Order(order_date=today, order_time=timestamp, user=request.user.id, item_name=item.size_name, item_category=item.size_category, item_size=item_size, item_toppings_num=item_tops_num, item_toppings_list=item_toppings, item_total_price=item_price)
    except KeyError:
        return render(request, 'orders/error.html')
    order.save()
    return redirect('index')

def shoppingcart(request):
    price_calc = Order.objects.filter(user=request.user.id).values('item_total_price')
    list_result = [entry for entry in price_calc]
    total_price = 0
    for x in list_result:
        for y in x.values():
            total_price += y
    context = {
        "user": request.user,
        "order": Order.objects.filter(user=request.user.id),
        "total": total_price,
    }
    return render(request, 'orders/shoppingcart.html', context)

def confirmorder(request):
    data = request.POST['checkout']
    if data == "complete":
        order = Order.objects.filter(user=request.user.id)
        full_name = request.user.first_name + ' ' + request.user.last_name
        order_num = int(d.datetime.now().timestamp())
        for x in order:
            today = date.today()
            timestamp = datetime.now().time()
            confirmed = Confirmed(order_number=order_num, order_date=today, order_time=timestamp, user=request.user.id, user_name= full_name, item_name=x.item_name, item_category=x.item_category, item_size=x.item_size, item_toppings_num=x.item_toppings_num, item_toppings_list=x.item_toppings_list, item_total_price=x.item_total_price)
            confirmed.save()
        Order.objects.filter(user=request.user.id).delete()
        return redirect('orders')

def dashboard(request):
    x = Confirmed.objects.order_by().values('order_number').distinct()
    y = [entry for entry in x]
    order_nums_list = []
    for i in y:
        for j in i.values():
            order_nums_list.append(j)

    z = Confirmed.objects.order_by().values('order_number', 'order_date', 'order_time', 'user').distinct()

    context = {
        "orders": Confirmed.objects.all(),
        "order_nums": order_nums_list,
        "order_dict": z,
    }
    return render(request, 'orders/dashboard.html', context)

def complete(request):
    order_id = request.POST['completeorder']
    completed_order = Confirmed.objects.filter(order_number =  order_id)
    for x in completed_order:
        today = date.today()
        timestamp = datetime.now().time()
        completed = Complete(order_number=x.order_number, order_date=today, order_time=timestamp, user=x.user, user_name= x.user_name, item_name=x.item_name, item_category=x.item_category, item_size=x.item_size, item_toppings_num=x.item_toppings_num, item_toppings_list=x.item_toppings_list, item_total_price=x.item_total_price)
        completed.save()
    Confirmed.objects.filter(order_number=order_id).delete()
    return redirect('dashboard')

def orders(request):
    pending_orders = Confirmed.objects.filter(user = request.user.id)
    complete_orders = Complete.objects.filter(user = request.user.id)

    x = Confirmed.objects.filter(user = request.user.id).order_by().values('order_number').distinct()
    y = [entry for entry in x]
    order_nums_pending = []
    for i in y:
        for j in i.values():
            order_nums_pending.append(j)

    n = Complete.objects.filter(user = request.user.id).order_by().values('order_number').distinct()
    m = [entry for entry in n]
    order_nums_complete = []
    for j in m:
        for i in j.values():
            order_nums_complete.append(i)

    context = {
        "pending": pending_orders,
        "complete": complete_orders,
        "pending_nums": order_nums_pending,
        "complete_nums": order_nums_complete,
    }
    return render(request, 'orders/ordered.html', context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You Have Been Registered'))
            return redirect('index')
    else:
        form = SignUpForm()
    
    context = {'form': form}
    return render(request, 'orders/register.html', context)
