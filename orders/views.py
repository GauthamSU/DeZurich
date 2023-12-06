from django.shortcuts import render
from menu.models import MenuItems
from django.utils.safestring import mark_safe
from static.pyscript.htmlstrings import html1, html2, html3
from django.forms.models import model_to_dict

# Create your views here.
def initiate_order(request):
    food = MenuItems.objects.filter(category='FOOD')
    drinks = MenuItems.objects.filter(category='DRINKS')
    hookah = MenuItems.objects.filter(category='HOOKAH')
    html_safe1 = mark_safe(html1)
    html_safe2 = mark_safe(html2)
    html_safe3 = mark_safe(html3)
    context = {'food':food, 'drinks':drinks, 'hookah':hookah, 'html1':html_safe1, 'html2':html_safe2, 'html3':html_safe3}
    return render(request, 'orders/order.html', context)


def track_order(request):
    context = {}
    return render(request, 'orders/order_track.html', context)