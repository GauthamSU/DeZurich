from django import forms
from .models import MenuItems
from django.forms.widgets import FileInput

input_class = "w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md"

class MenuItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'placeholder':'Enter the Title', 'class':input_class})
        self.fields['description'].widget.attrs.update({'placeholder':'Describe the dish', 'class':input_class})
        self.fields['price'].widget.attrs.update({'placeholder':'Enter the price', 'class':input_class})
        self.fields['category'].widget.attrs.update({'class':input_class})
        self.fields['sub_category'].widget.attrs.update({'class':input_class})
        self.fields['is_non_veg'].widget.attrs.update({'class':input_class})

    class Meta:
        model = MenuItems
        fields = '__all__'
        widgets = {
            'dish_image': FileInput(attrs={'class':"block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400"})
        }