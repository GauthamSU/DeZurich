from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from .forms import MenuItemForm, EditMenuItemForm, MenuFilterForm
from .models import MenuItems, FOOD_SUBCAT_CHOICES, DESSERT_SUBCAT_CHOICES, DRINKS_SUBCAT_CHOICES
from .filters import ItemFilter

def menu_items(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(form.cleaned_data['dish_image'])
            return redirect('menu-add')
        else:
            print(form.errors)
    else:
        form = MenuItemForm()
    context = {'form':form, 
               'food_subcat': FOOD_SUBCAT_CHOICES,
               'drinks_subcat': DRINKS_SUBCAT_CHOICES,
               'dessert_subcat': DESSERT_SUBCAT_CHOICES}
    return render(request, 'menu/menu_input.html', context)


def raw_menu_items_view(request):
    menu_items = MenuItems.objects.all()
    EditMenuFormset = modelformset_factory(MenuItems, form=EditMenuItemForm)
    formset = EditMenuFormset()
    if request.method == 'POST':
        formset = EditMenuFormset(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()

        return redirect('menu-edit')
    
    items_filter = ItemFilter(request.GET, queryset=menu_items)
    context_data = zip(items_filter.qs, formset)
    context = {
                'context_data':context_data, 
                'filter_form':items_filter.form,
                'food_subcat': FOOD_SUBCAT_CHOICES,
                'drinks_subcat': DRINKS_SUBCAT_CHOICES,
                'dessert_subcat': DESSERT_SUBCAT_CHOICES
               }
    return render(request, 'menu/update_menu.html', context)


def menu_consumer(request):
    
    items = MenuItems.objects.all()
    food_items = items.filter(category='FOOD')
    drinks_items = items.filter(category='DRINKS')
    dessert_items = items.filter(category='DESSERT')
    hookah_items = items.filter(category='HOOKAH')
    context = {'food_items':food_items, 
               'drinks_items': drinks_items, 
               'dessert_items':dessert_items, 
               'hookah_items':hookah_items,
               'food_subcat': FOOD_SUBCAT_CHOICES,
               'drinks_subcat': DRINKS_SUBCAT_CHOICES,
               'dessert_subcat': DESSERT_SUBCAT_CHOICES}
    return render(request, 'menu/menu_view.html', context)