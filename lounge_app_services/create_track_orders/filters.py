import django_filters
from django.forms import widgets
from lounge_app_services.menu.models import (
    MenuItems, 
    FOOD_SUBCAT_CHOICES, 
    DRINKS_SUBCAT_CHOICES, 
    DESSERT_SUBCAT_CHOICES, 
    )

class FoodOrderFilter(django_filters.FilterSet):
    # title = django_filters.CharFilter(
    #     widget=widgets.TextInput(attrs={'hx-include':"#food-filter-form, #food-items-list [type='number']"})
    #     )
    sub_category = django_filters.ChoiceFilter(
        choices=FOOD_SUBCAT_CHOICES#,
        # widget=widgets.Select(attrs={'hx-include':"#food-filter-form, #food-items-list [type='number']"})
        )
    # is_non_veg = django_filters.BooleanFilter(
    #     widget=widgets.NullBooleanSelect(attrs={'hx-include':"#food-filter-form, #food-items-list [type='number'], #food-items-list [data-input-type='preference']"})
    #     )
    class Meta:
        model = MenuItems
        fields = {'title':['icontains'], 'sub_category':['exact'], 'is_non_veg':['exact']}



class DrinksDessertOrderFilter(django_filters.FilterSet):
    sub_category = django_filters.ChoiceFilter(
        choices=DRINKS_SUBCAT_CHOICES + DESSERT_SUBCAT_CHOICES
    )
    class Meta:
        model = MenuItems
        fields = {'title':['icontains'], 'sub_category':['exact']}


class HookahOrderFilter(django_filters.FilterSet):
    class Meta:
        model = MenuItems
        fields = {'title':['icontains']}