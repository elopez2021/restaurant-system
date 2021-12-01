from django.contrib import admin

# Register your models here.
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image_tag')

admin.site.register(Category, CategoryAdmin)

class DishAdmin(admin.ModelAdmin):
    list_display = ('id','name','price', 'status','is_featured')
    list_editable = ('status', 'is_featured')

admin.site.register(Dish, DishAdmin)
admin.site.register(Ingredient)
admin.site.register(Supplier)