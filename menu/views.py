from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from .forms import MenuItemForm, EditMenuItemForm
from .models import MenuItems

# Create your views here.
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
    if request.method == 'POST':
        formset = EditMenuFormset(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()

        return redirect('menu-edit')
    else:
        formset = EditMenuFormset()
    context_data = zip(menu_items, formset)
    context = {'context_data':context_data}
    return render(request, 'menu/update_menu.html', context)