from django.urls import path
from .views import menu_items, raw_menu_items_view

urlpatterns = [
    path('add/', menu_items, name='menu-add'),
    path('edit/', raw_menu_items_view, name="menu-edit"),
]