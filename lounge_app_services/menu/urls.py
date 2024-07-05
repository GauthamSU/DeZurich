from django.urls import path, include
from .views import menu_items, raw_menu_items_view, menu_consumer

urlpatterns = [
    path('', menu_consumer, name="menu"),
    path('add/', menu_items, name='menu-add'),
    path('edit/', raw_menu_items_view, name="menu-edit"),
]