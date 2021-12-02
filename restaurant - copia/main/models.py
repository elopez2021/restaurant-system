from django.db import models

# Create your models here.
from django.utils.html import mark_safe #import this to show the image next to the category object and mark_safe send data safely
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="cat_imgs/") #gotta install pillow, pip install pillow
    class Meta:
        verbose_name_plural = 'Categories'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
   
    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True, blank=True)
    price = models.FloatField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="dish_img/") #gotta install pillow, pip install pillow
    price = models.FloatField()
    slug = models.SlugField(max_length=400, null=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    ingredient = models.ManyToManyField(Ingredient)
    quantity = models.PositiveIntegerField()
    status = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Dishes'

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    id_card = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    ingredient = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name

class DrinkCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category_drink_imgs/")
    size = models.PositiveIntegerField()
    calories = models.PositiveIntegerField()
class Drink(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="drink_img/")
    category = models.ForeignKey(DrinkCategory, on_delete=models.CASCADE)
    size = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
