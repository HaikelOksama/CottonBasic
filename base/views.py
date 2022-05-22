
import random
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .models import Product, Cart
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q 
# Create your views here.

def home(request):
    product = Product.objects.all()
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            cart = Cart.objects.get(id=request.user.id)
            product = Product.objects.get(id=request.POST['add'])
            cart.products.add(product)
            return redirect('cart', request.user.id)
        else:
            return redirect('login')

    context = {
        'products' : product,
    }
    return render(request, 'base/home.html', context)

def productView(request):
    
    q = request.GET.get('sort') if request.GET.get('sort') != None else ''
    w = request.GET.get('q') if request.GET.get('q') != None else ''
    
    product = list(Product.objects.all())
    if q == 'new':
        product = list(Product.objects.all().order_by('-created'))
    elif q == 'lowest':
        product = list(Product.objects.all().order_by('price','discountedPrice'))
    elif q == 'highest':
        product = list(Product.objects.all().order_by('-price'))

    wanted = random.sample(product, 3)
        
    if  w:
        product = list(Product.objects.filter(
            Q(name__icontains = w)
        ))
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            cart = Cart.objects.get(id=request.user.id)
            product = Product.objects.get(id=request.POST['add'])
            cart.products.add(product)
            return redirect('cart', request.user.id)
        else:
            return redirect('login')
    context = {
        'wanted': wanted,
        'products' : product,
    }
    return render(request, 'base/product.html', context)

@login_required(login_url='login')
def cart(request, pk):
    # user = User.objects.get(username = customer)
    # cart = user.cart_set.all()
    
    cart = Cart.objects.get(id=pk)
    product = cart.products.all()
    
    if request.user != cart.customer:
        return redirect('home') 
    
    if request.method == 'POST':
        product = cart.products.get(id=request.POST['delete'])
        cart.products.remove(product)
        return redirect('cart', request.user.id)
    
    context = {
        'products' : product,

    }
    return render(request, 'base/cart.html', context)

@login_required(login_url='login')
def remove(request, pk):
    cart = Cart.objects.get(id=request.user.id)
    product = cart.products.get(id=pk)
    if request.method == 'POST':
        cart.products.remove(product)
        return redirect('cart', request.user.id)
    context = {
        'product' : product,
    }
    
    return render(request, 'base/remove.html', context)


def detail(request, pk):
    product = Product.objects.get(id=pk)

    if request.user.is_authenticated:
        cart = Cart.objects.get(id = request.user.id)
    else:
        cart = Cart.objects.get(id = 1)

    if request.method == 'POST':
        cart.products.add(product)
        print(product.itemCount)
        return redirect('cart', request.user.id)

    context = {
        'product' : product,
    }
    return render(request, 'base/detail.html', context)

def testimoniView(request):
    return render(request, 'base/testimonial.html', {})

def aboutView(request):
    return render(request, 'base/about.html', {})

def contactView(request):
    return render(request, 'base/contact.html', {})

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is wrong')
    context = {}
    return render(request, 'base/login.html', context)

@login_required(login_url='login')
def profileView(request, user):
    user = User.objects.get(username = user)
    context = {
        'user' : user,
    }
    return render(request, 'base/profile.html', context)

def registerUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    forms = UserCreationForm()
    if request.method == "POST":
        forms = UserCreationForm(request.POST)
        if forms.is_valid():
            newUser = forms.save(commit=False)
            
            newUser.username.lower()
            newUser.save()

            cart = Cart.objects.create(
                customer = newUser,        
            )
            cart.save()

            return redirect('login')

    context={
        'forms' : forms,
    }
    return render(request, 'base/register.html', context)

def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')
    return redirect('home')
    
