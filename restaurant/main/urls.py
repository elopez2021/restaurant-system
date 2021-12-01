from django.urls import path
from . import views

from django.conf import settings #import settings
from django.conf.urls.static import static #you need to import this if you  wanna use static files through a url

urlpatterns=[
    path('', views.home, name='home'),
    path('category-list', views.category_list, name='category-list'),
    path('dishes-list', views.dishes_list, name='dishes-list'),
    path('category-dish-list/<int:cat_id>/', views.category_dish_list, name='category-dish-list'),
]
#this is important for static files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)