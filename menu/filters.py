import django_filters
from django import forms
from .models import MenuItems, subcat_choices

class ItemFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()
    sub_category = django_filters.MultipleChoiceFilter(
        choices=subcat_choices,
        widget=forms. CheckboxSelectMultiple())

    class Meta:
        model = MenuItems
        fields = {'title':['icontains'], 'category':['exact'], 'sub_category':['exact'], 'is_non_veg':['exact']}
        