import pytest
from lounge_app_services.menu.models import MenuItems
from django.utils.text import slugify


@pytest.mark.django_db
def test_create_menu_items(create_menu_items):
    assert create_menu_items.slug_title == slugify(create_menu_items.title + ' ' + str(create_menu_items.sub_category) + ' ' + str(create_menu_items.is_non_veg))
    print(create_menu_items.price)