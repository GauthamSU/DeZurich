from django.urls import path
from .views import menu_items

urlpatterns = [
    path('menu/', menu_items, name='menu'),
]