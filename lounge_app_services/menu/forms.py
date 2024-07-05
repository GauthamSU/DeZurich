from django import forms
from .models import MenuItems
from django.forms import modelformset_factory
from django.forms.widgets import FileInput, Textarea, CheckboxInput
from django_select2 import forms as s2forms

class SubCategoryWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = ["sub_category__icontains"]
    model = MenuItems
    

class MenuItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'placeholder':'Enter the Title'})
        self.fields['description'].widget.attrs.update({'placeholder':'Describe the dish'})
        self.fields['price'].widget.attrs.update({'placeholder':'Enter the price'})
        
    class Meta:
        model = MenuItems
        fields = '__all__'
        widgets = {
            'dish_image': FileInput(attrs={'onchange':"previewImage()"}),
            # 'sub_category': SubCategoryWidget()
            'sub_category': s2forms.Select2Widget(attrs={
                'data-selection-css-class': ":all:"
            }),
            'is_non_veg': CheckboxInput()
        }


class EditMenuItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'placeholder':'Enter the Title'})
        self.fields['price'].widget.attrs.update({'placeholder':'Enter the price'})
        

    class Meta:
        model = MenuItems
        fields = '__all__'
        widgets = {
            'dish_image': FileInput(),
            'description':Textarea(attrs={'placeholder':'Describe the dish'}),
            'is_non_veg': CheckboxInput()
        }


class MenuFilterForm(forms.ModelForm):
    class Meta:
        model = MenuItems
        fields = ('category', 'sub_category')