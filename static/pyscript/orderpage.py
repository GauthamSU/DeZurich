from pyscript import window, when, display
import js
from js import document, Cookies
import requests
import pyodide_http
import re

def string_to_slug(input_string):
    result = input_string.lower()
    result = re.sub(r'[^a-z0-9\s-]', '', result)
    result = result.replace(' ', '-')
    return result


pyodide_http.patch_all()

data_dict = {}
modal_html = """
<li id="slugified_name">
    <div class="grid grid-cols-5 justify-between items-center w-full p-1 px-2 text-gray-900 bg-white border border-gray-200 rounded-lg dark:border-gray-500 dark:text-white dark:bg-gray-600">
        <p class="col-span-3">item_name</p>
        <div class="flex justify-center gap-1 col-span-1">
            <p>item_quantity</p>
            <p>x</p>
            <p>individual_item_price</p>
        </div>
        <p class="col-span-1 text-right">total_item_price</p>
    </div>
    <div class="p-1 px-2 hidden">
        <span class="px-10 py-0\.5 text-center text-gray-700 bg-gray-100 border border-gray-200 rounded-lg dark:border-gray-500 dark:text-gray-100 dark:bg-gray-400 preference_target"></span>
    </div>
</li>
"""
modal_segregate = """
<p class="dark:text-white text-gray-900 text-lg font-medium" id="ordered_id">modal_type Ordered: </p> 
"""

@when('click', '.minus')
def reduce(event):
    ele = event.target
    quantity_element = ele.parentNode.getElementsByClassName('quantity')[0]
    quantity = int(quantity_element.value)
    if quantity > 0:
        quantity -= 1
        quantity_element.value = quantity
        if quantity == 0:
            pref_el = ele.parentNode.parentNode.parentNode.getElementsByClassName('preference')[0]
            pref_el.disabled = True
            preference_input = ele.parentNode.parentNode.parentNode.parentNode.getElementsByClassName('preference_input')[0]
            if not 'hidden' in preference_input.classList:
                preference_input.classList.add('hidden')
    order_total(ele, quantity)
        

@when('click', '.plus')
def increase(event):
    ele = event.target
    quantity_element = ele.parentNode.getElementsByClassName('quantity')[0]
    quantity = int(quantity_element.value)
    quantity += 1
    quantity_element.value = quantity
    ele.parentNode.parentNode.parentNode.getElementsByClassName('preference')[0].disabled = False
    order_total(ele, quantity)


table_num = document.getElementById('table_number').value
if int(table_num) == 0:
    document.getElementById('preview_button').disabled = True


@when('change', '#table_number')
def change_disable():
    table_num = document.getElementById('table_number').value
    if int(table_num) == 0:
        document.getElementById('preview_button').disabled = True
    else:
        document.getElementById('preview_button').disabled = False
        document.getElementById('popover-top').classList.add('hidden')



@when('click', '#preview_button')
def get_table_num():
    table_num = document.getElementById('table_number').value
    document.getElementById('modal_table_num').innerHTML = f"Table Number : {table_num}"
    amount_element = document.getElementById('total_amount').innerHTML
    document.getElementById('order_total').innerHTML = f"Order Total : {amount_element.split()[-1]}"
    

@when('click', '#submit_botton')
def send_request():
    csrftoken = Cookies.get('csrftoken')
    complete_url = window.location.href
    requests.post(url=complete_url, data=data_dict, headers={"X-CSRFToken": csrftoken})
    

@when('mouseover', '#submit_botton')
def disable_submit_button():
    total_quantity = document.getElementById('num_items').textContent
    if int(total_quantity.split()[-1]) == 0:
        document.getElementById('submit_botton').disabled = True
    else:
        document.getElementById('submit_botton').disabled = False
        document.getElementById('popover-bottom').classList.add('hidden')


@when('change', '.preference_input')
def add_preference_to_modal(event):
    target_element = event.target
    target_title = target_element.parentNode.parentNode.getElementsByClassName('menu-item')[0].textContent
    slugified_item = string_to_slug(target_title)
    preference_target = document.getElementById(slugified_item).getElementsByClassName('preference_target')[0]
    preference_target.innerHTML = target_element.value
    preference_target.parentNode.classList.remove('hidden')


@when('click', '.preference')
def show_preference_input(event):
    target_element = event.target
    hidden_element = target_element.parentNode.parentNode.parentNode.getElementsByClassName('preference_input')[0]
    if 'hidden' in hidden_element.classList:
        hidden_element.classList.remove('hidden')
    else:
        hidden_element.classList.add('hidden')


def order_total(target_element, quantity):
    parent =  target_element.parentNode.parentNode.parentNode
    parent_id = parent.parentNode.parentNode.getAttribute('id')
    if parent_id == 'food_items':
        item_type = 'FOOD'
        modal_id = 'food_list'
        ordered_id = 'food_ordered'
    elif parent_id == 'drinks_items':
        item_type = 'DRINKS'
        modal_id = 'drinks_list'
        ordered_id = 'drinks_ordered'
    else:
        item_type = 'HOOKAH'
        modal_id = 'hookah_list'
        ordered_id = 'hookah_ordered'

    order_item = parent.getElementsByClassName('menu-item')[0].textContent
    slug_item_name = string_to_slug(order_item)
    price = parent.getElementsByClassName('price')[0].textContent
    total = round((quantity * float(price)), 2)
    data_dict[order_item] = [quantity, float(price), total, item_type]
    # data_dict[order_item] = {'quantity':quantity, 'price':float(price), 'Total':total, 'Type':item_type}
    final_total = round(sum([val[2] for val in data_dict.values()]), 2)
    final_quant = sum(quant[0] for quant in data_dict.values())
    
    final_items = document.getElementById('num_items')
    final_items.textContent = f"Number of items ordered: {final_quant}"
    
    final_amount = document.getElementById('total_amount')
    final_amount.textContent = f"Total Amount: {final_total}"
    
    order_item_li = document.getElementById(slug_item_name)
    if not order_item_li:
        if parent_id == 'food_items':       
            food_ordered = document.getElementById(ordered_id)
            if not food_ordered:
                modal_type = modal_segregate.replace('modal_type', 'Food')
                modal_type = modal_type.replace('ordered_id', ordered_id)
                document.getElementById(modal_id).innerHTML += modal_type
        elif parent_id == 'drinks_items':
            
            drinks_ordered = document.getElementById(ordered_id)
            if not drinks_ordered:
                modal_type = modal_segregate.replace('modal_type', 'Drinks')
                modal_type = modal_type.replace('ordered_id', ordered_id)
                document.getElementById(modal_id).innerHTML += modal_type
        else:
            
            drinks_ordered = document.getElementById(ordered_id)
            if not drinks_ordered:
                modal_type = modal_segregate.replace('modal_type', 'Hookah')
                modal_type = modal_type.replace('ordered_id', ordered_id)
                document.getElementById(modal_id).innerHTML += modal_type

        render_html = modal_html.replace('item_name', order_item)
        render_html = render_html.replace('slugified_name', slug_item_name)
        render_html = render_html.replace('item_quantity', str(quantity))
        render_html = render_html.replace('individual_item_price', str(price))
        render_html = render_html.replace('total_item_price', str(total))
        document.getElementById(modal_id).innerHTML += render_html
    else:
        if quantity == 0:
            order_item_li.remove()
        else:
            paras = order_item_li.getElementsByTagName('p')
            if order_item in paras[0].textContent:
                paras[1].textContent = quantity
                paras[-1].textContent = total

