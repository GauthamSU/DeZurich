from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from .forms import MenuItemForm, EditMenuItemForm
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
    originating_url = request.META.get('HTTP_REFERER')
    items_filter = ItemFilter(request.GET, queryset=menu_items)
    context = {
                'item_queryset':items_filter.qs, 
                'filter_form':items_filter.form,
                'originating_url':originating_url,
                'food_subcat': FOOD_SUBCAT_CHOICES,
                'drinks_subcat': DRINKS_SUBCAT_CHOICES,
                'dessert_subcat': DESSERT_SUBCAT_CHOICES
               }
    
    return render(request, 'menu/update_menu.html', context)


def menu_edit_form_view(request, slug_title):
    menu_item = MenuItems.objects.get(slug_title=slug_title)
    originating_url = request.META.get('HTTP_REFERER')
    # print(originating_url)
    if request.method == 'GET':
        form=EditMenuItemForm(instance=menu_item)
    if request.method == 'POST':
        form = EditMenuItemForm(request.POST, request.FILES, instance=menu_item)
        if form.is_valid():
            if request.FILES:
                if request.FILES.get('dish_image'):
                    menu_item.dish_image = request.FILES['dish_image']
                menu_item.save()
            form.save()
            pk = menu_item.pk
            slug_title = MenuItems.objects.get(pk=pk).slug_title
            return redirect('menu-card-details', slug_title)
        else:
            print(form.errors)
    return render(request, 'menu/menu_partials/menu_filter_partial.html#item-edit-form', {'form':form, 'originating_url':originating_url})


def menu_edit_card_view(request, slug_title):
    menu_item = MenuItems.objects.get(slug_title=slug_title)
    # if request.DELETE:
    #     MenuItems.delete(instance=menu_item)
    
    return render(request, 'menu/menu_partials/menu_filter_partial.html#item-card-view', {'item':menu_item})



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