from django.shortcuts import render
from lounge_app_services.menu.models import MenuItems

# Create your views here.
def index(request):
    # menu_items = MenuItems()
    items = MenuItems.objects.all()
    food_items = items.filter(category='FOOD')
    drinks_items = items.filter(category='DRINKS')
    dessert_items = items.filter(category='DESSERT')
    hookah_items = items.filter(category='HOOKAH')
    context = {'food_items':food_items, 
               'drinks_items': drinks_items, 
               'dessert_items':dessert_items, 
               'hookah_items':hookah_items}
    return render(request, 'homepage/index.html', context)