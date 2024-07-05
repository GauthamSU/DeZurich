import django_filters
from django import forms

from .models import MenuItems, SUBCAT_CHOICES
from django_select2 import forms as s2forms

class ItemFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()
    sub_category = django_filters.MultipleChoiceFilter(
        choices=SUBCAT_CHOICES,
        widget=s2forms.Select2MultipleWidget())
    # is_non_veg = django_filters.BooleanFilter(
    #     widget=forms.widgets.CheckboxInput()
    # )

    class Meta:
        model = MenuItems
        fields = {'title':['icontains'], 'category':['exact'], 'sub_category':['exact'], 'is_non_veg':['exact']}

        