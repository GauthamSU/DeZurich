from django.shortcuts import render
from menu.models import MenuItems

# Create your views here.
def index(request):
    # menu_items = MenuItems()
    items = MenuItems.objects.all()
    context = {'items':items}
    return render(request, 'index.html', context)