from django.shortcuts import render
from .models import Category, Dish

# Create your views here.
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