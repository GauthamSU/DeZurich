from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from django.http import JsonResponse
from lounge_app_services.menu.models import MenuItems, CATEGORY_CHOICES
from .models import OrderDetails, OrderItem
from django.contrib import messages
from .forms import OrderItemForm
from .filters import FoodOrderFilter, DrinksDessertOrderFilter, HookahOrderFilter

# from .serializers import OrderSerializer

def initiate_order(request):
    menu_items = MenuItems.objects.all()
    food_order_filters = FoodOrderFilter(request.GET, queryset=menu_items.filter(category='FOOD'))
    drinks_dessert_order_filters = DrinksDessertOrderFilter(request.GET, queryset=menu_items.filter(category__in=['DRINKS', 'DESSERT']))
    hookah_order_filters = HookahOrderFilter(request.GET, queryset=menu_items.filter(category='HOOKAH'))
    context = {'menu_items':menu_items, 
               'food_order_filters':food_order_filters.form,
               'drinks_dessert_order_filters':drinks_dessert_order_filters.form,
               'hookah_order_filters':hookah_order_filters.form
               }
    
    if request.method == 'POST':
        item_list = []
        category_list = []
        quantity_list = []
        item_price_list = []
        item_title_list = []
        is_non_veg_list =[]
        preference_list = []
        item_price_total_list = []
        ordered_dict = dict(request.POST)
        table_num = int(ordered_dict['table-number'][0])
        
        total_quantity = 0
        total_amount = 0
        employee = request.user.userprofile

        if not request.htmx and table_num > 0:
            order = OrderDetails.objects.create(employee=employee, table_num=table_num) #, total_quantity=total_quantity, order_total=total_amount)
        
        for item, value in ordered_dict.items():
            if 'quantity' in item and int(value[0]) > 0:
                slug_title = item.replace('quantity-', '')
                item_list.append(slug_title)
                
                quantity = int(value[0])
                quantity_list.append(quantity)

                preference = ordered_dict[f'preference-{slug_title}'][0]
                preference_list.append(preference)
                
                menu_item = MenuItems.objects.get(slug_title=slug_title)

                item_price = round(float(menu_item.price), 2)
                item_price_list.append(item_price)

                category = menu_item.category
                category_list.append(category)

                item_title = menu_item.title
                item_title_list.append(item_title)

                is_non_veg = menu_item.is_non_veg
                is_non_veg_list.append(is_non_veg)

                item_order_price = item_price * quantity
                item_price_total_list.append(item_order_price)

                total_quantity += quantity
                total_amount += item_order_price
                
                if not request.htmx:
                    OrderItem.objects.create(order=order, product=menu_item, quantity=quantity, order_price=item_order_price, preference=preference)
        
        # Returns the ordered list for the preview
        if request.htmx and table_num > 0:
            context = {'data': list(zip(item_list, category_list, quantity_list, item_price_list, item_title_list, is_non_veg_list, preference_list, item_price_total_list)),
                        'total_amount': total_amount,
                        'total_quantity': total_quantity,
                        'table_number': table_num
                        }
            return render(request, 'create_track_orders/partials/create_order_partial.html#preview-modal', context)
        

        if table_num > 0 and total_quantity > 0:
            items_ordered = MenuItems.objects.filter(slug_title__in = item_list)
            order.title.set(items_ordered)
            order.save()

            messages.add_message(request, messages.INFO, order.order_id)
            return redirect('track-order')
        

    return render(request, 'create_track_orders/new_order.html', context) 



def track_order(request):
    data = messages.get_messages(request)
    recent_order = OrderDetails.objects.exclude(order_status__in=['order_paid', 'order_completed'])
    message = ''
    if data:
        for d in data:
            message = d
    
    context = {'recent_order':recent_order, 'cat_choices':CATEGORY_CHOICES, 'message':message}
    
    return render(request, 'create_track_orders/order_track.html', context)



def order_filter_view(request, category):
    if category == 'FOOD':
        menu_items = MenuItems.objects.filter(category=category)
        order_filters = FoodOrderFilter(request.GET, queryset=menu_items)
    elif category == 'DRINKS':
        menu_items = MenuItems.objects.filter(category__in=['DRINKS', 'DESSERT'])
        order_filters = DrinksDessertOrderFilter(request.GET, queryset=menu_items)
        category = "DRINKS DESSERT"
    else:
        menu_items = MenuItems.objects.filter(category=category)
        order_filters = HookahOrderFilter(request.GET, queryset=menu_items)
    # context = {'order_filter_queryset': order_filters.qs, 
    #            'order_filter_form':order_filters.form,
    #            'category': category,
    #            'menu_items':menu_items}
    excluded_queryset = menu_items.difference(order_filters.qs)    
    context = {'order_filter_queryset': list(order_filters.qs.values()),
               'excluded_queryset':list(excluded_queryset.values())}
    # return render(request, 'create_track_orders/partials/create_order_partial.html#filtered-list-partial', context=context)
    return JsonResponse(context, safe=False)