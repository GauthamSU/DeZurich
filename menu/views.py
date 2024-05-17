from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from .forms import MenuItemForm, EditMenuItemForm, MenuFilterForm
from .models import MenuItems
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
    context = {'form':form}
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
    context = {'context_data':context_data, 'filter_form':items_filter.form}
    return render(request, 'menu/update_menu.html', context)


