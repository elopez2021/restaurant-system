from django.shortcuts import render
from .models import Category

# Create your views here.
def home(request):
    return render(request, 'main/index.html')

#Category
def category_list(request):
    category=Category.objects.all().order_by('id')
    return render(request, 'main/category-list.html', {'category':category})