from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="cat_imgs/") #gotta install pillow, pip install pillow

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True, blank=True)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="dish_img/") #gotta install pillow, pip install pillow
    price = models.FloatField()
    description = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    ingredient = models.ManyToManyField(Ingredient)
    quantity = models.IntegerField()
    status = models.BooleanField(default=True)

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