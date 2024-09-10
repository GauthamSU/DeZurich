import pytest
from lounge_app_services.menu.factories import MenuItemsFactory

@pytest.fixture
def create_menu_items():
    return MenuItemsFactory()