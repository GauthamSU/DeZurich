import pytest
from lounge_app_services.menu.models import MenuItems
from lounge_app_services.create_track_orders.factories import OrderDetailsFactory, OrderItemFactory


@pytest.fixture
def place_new_order():
    menu_items = MenuItems.objects.all()
    return OrderDetailsFactory.create(set_title=menu_items)