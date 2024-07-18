from django.urls import path, include
from django.urls import path, include
from .views import menu_edit_form_view, menu_edit_card_view

urlpatterns = [
    path('<slug:slug_title>/', menu_edit_form_view, name="menu-edit-details"),
    path('card/<slug:slug_title>/', menu_edit_card_view, name="menu-card-details")
]