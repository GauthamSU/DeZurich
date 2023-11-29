from django.shortcuts import render, redirect
from .forms import MenuItemForm

# Create your views here.
def menu_items(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(form.cleaned_data['dish_image'])
            return redirect('menu')
        else:
            print(form.errors)
    else:
        form = MenuItemForm()
    context = {'form':form}
    return render(request, 'menu/menu_input.html', context)