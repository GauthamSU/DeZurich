import pytest
from lounge_app_services.menu.models import MenuItems
from django.utils.text import slugify


@pytest.mark.django_db
def test_create_menu_items(place_new_order):
    print(place_new_order.order_placed, place_new_order.order_prepared, place_new_order.order_completed)
    print(place_new_order.title)