from django.urls import path, include
from .views import menu_items, raw_menu_items_view, menu_consumer, menu_edit_form_view, menu_edit_card_view

urlpatterns = [
    path('', menu_consumer, name="menu"),
    path('add/', menu_items, name='menu-add'),
    path('edit/', raw_menu_items_view, name="menu-edit"),
    path('edit/', include('lounge_app_services.menu.htmx_urls'))
]

