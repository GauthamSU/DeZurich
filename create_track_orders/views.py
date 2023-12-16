from django.shortcuts import render, redirect
from menu.models import MenuItems
from .models import OrderDetails, OrderItem
from django.contrib import messages

from .serializers import OrderSerializer

def initiate_order(request):
    menu_items = MenuItems.objects.all()
    context = {'menu_items':menu_items}
    if request.method == 'POST':
        item_list = []
        ordered_dict = dict(request.POST)
        table_num = int(ordered_dict['table-number'][0])
        total_quantity = int(ordered_dict['total-items'][0])
        total_amount = round(float(ordered_dict['total-amount'][0]), 2)
        employee = request.user.userprofile
        order = OrderDetails.objects.create(employee=employee, table_num=table_num, total_quantity=total_quantity, order_total=total_amount)
        for item, value in ordered_dict.items():
            if 'quantity' in item and int(value[0]) > 0:
                slug_title = item.replace('quantity-', '')
                item_list.append(slug_title)
                menu_item = MenuItems.objects.get(slug_title=slug_title)
                quantity = int(value[0])
                preference = ordered_dict[f'preference-{slug_title}'][0]
                order_price = round(float(ordered_dict[f'price-{slug_title}'][0]), 2) * quantity
                order_item = OrderItem.objects.create(order=order, product=menu_item, quantity=quantity, order_price=order_price, preference=preference)
        items_ordered = MenuItems.objects.filter(slug_title__in = item_list)
        order.title.set(items_ordered)
        order.save()

        messages.add_message(request, messages.INFO, order.order_id)
        return redirect('track-order')
    return render(request, 'create_track_orders/new_order.html', context) 

def track_order(request):
    data = messages.get_messages(request)
    recent_order = OrderDetails.objects.exclude(order_status='order_paid')
    message = ''
    if data:
        for d in data:
            message = d
    
    context = {'recent_order':recent_order, 'message':message}
    
    # recent_order = OrderDetails.objects.first()
    # recent_order_items = OrderItem.objects.filter(order=recent_order)
    # serialized_data = OrderSerializer(recent_order)
    
    return render(request, 'create_track_orders/order_track.html', context)
