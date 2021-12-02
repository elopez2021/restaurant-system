from django.shortcuts import render, redirect
from .models import Category, Dish
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm

# Create your views here.
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            
            username = request.POST.get('username')
            password = request.POST.get('password1')
            
            new_user = authenticate(request, username=username, password=password)
            login(request, new_user)
            return redirect('home')
        
    context = {'form':form}
    return render(request, 'main/register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
           # messages.info(request, 'Usuario o contraseña incorrecta')
           pass

    context = {}
    return render(request, 'main/login.html', context)


def home(request):
    data=Dish.objects.filter(is_featured=True).order_by('-id')
    return render(request, 'main/index.html', {'data':data})

#Category
def category_list(request):
    category=Category.objects.all().order_by('id')
    return render(request, 'main/category-list.html', {'category':category})

#Product List
def dishes_list(request):
    dishes=Dish.objects.all().order_by('-id')
    cats=Dish.objects.distinct().values('category__name', 'category__id') #because the category name is a foreign key we add __ to fetch the field
    ingres=Dish.objects.distinct().values('ingredient__name', 'ingredient__id')
    context = {'dishes':dishes, 'cats':cats, 'ingres':ingres}

    return render(request, 'main/dishes-list.html', context)

# Dishes List According to Category
def category_dish_list(request, cat_id):
    category=Category.objects.get(id=cat_id) #this has to be an instance of Category 
    dishes=Dish.objects.filter(category=category).order_by('-id') #and here we pass the category instance
    cats=Dish.objects.distinct().values('category__name', 'category__id')
    ingres=Dish.objects.distinct().values('ingredient__name', 'ingredient__id')
    context = {'dishes':dishes, 'cats':cats, 'ingres':ingres}
    return render(request, 'main/category_dish_list.html', context)

#Dishes Detail
def dish_detail(request,slug,id):
    dishes = Dish.objects.get(id=id)
    ingres=Dish.objects.distinct().values('ingredient__name', 'ingredient__id')
    cats=Dish.objects.distinct().values('category__name', 'category__id')
    context = {'dishes':dishes, 'ingres':ingres, 'cats':cats}
    return render(request, 'main/dish_detail.html', context)