from django.contrib import admin

# Register your models here.
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
admin.site.register(Category, CategoryAdmin)
'''
class DishAdmin(admin.ModelAdmin):
    list_display = ('id','name','image', 'status')
    list_editable = ('status')
'''

admin.site.register(Dish)
admin.site.register(Ingredient)
admin.site.register(Supplier)