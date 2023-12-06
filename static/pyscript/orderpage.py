from pyscript import window, when, display
import js
from js import document


data_dict = {}
modal_html = """
<li class="grid grid-cols-5 justify-between items-center w-full p-1 px-2 text-gray-900 bg-white border border-gray-200 rounded-lg dark:border-gray-500 dark:text-white dark:bg-gray-600">
    <p class="col-span-3">item_name</p>
    <div class="flex justify-center gap-1 col-span-1">
        <p>item_quantity</p>
        <p>x</p>
        <p>individual_item_price</p>
    </div>
    <p class="col-span-1 text-right">total_item_price</p>
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
    order_total(ele, quantity)
        

@when('click', '.plus')
def increase(event):
    ele = event.target
    quantity_element = ele.parentNode.getElementsByClassName('quantity')[0]
    quantity = int(quantity_element.value)
    quantity += 1
    quantity_element.value = quantity
    order_total(ele, quantity)

def order_total(target_element, quantity):
    parent =  target_element.parentNode.parentNode.parentNode
    order_item = parent.getElementsByClassName('menu-item')[0].textContent
    price = parent.getElementsByClassName('price')[0].textContent
    total = round((quantity * float(price)), 2)
    data_dict[order_item] = [quantity, float(price), total]
    final_total = round(sum([val[2] for val in data_dict.values()]), 2)
    final_quant = sum(quant[0] for quant in data_dict.values())
    
    final_items = document.getElementById('num_items')
    final_items.textContent = f"Number of items ordered: {final_quant}"
    
    final_amount = document.getElementById('total_amount')
    final_amount.textContent = f"Total Amount: {final_total}"
    
    parent_id = parent.parentNode.getAttribute('id')

    if data_dict[order_item][0] == 1:
        if parent_id == 'food_items':
            modal_id = 'food_list'
            ordered_id = 'food_ordered'
            food_ordered = document.getElementById(ordered_id)
            if not food_ordered:
                modal_type = modal_segregate.replace('modal_type', 'Food')
                modal_type = modal_type.replace('ordered_id', ordered_id)
                document.getElementById(modal_id).innerHTML += modal_type
        elif parent_id == 'drinks_items':
            modal_id = 'drinks_list'
            ordered_id = 'drinks_ordered'
            drinks_ordered = document.getElementById(ordered_id)
            if not drinks_ordered:
                modal_type = modal_segregate.replace('modal_type', 'Drinks')
                modal_type = modal_type.replace('ordered_id', ordered_id)
                document.getElementById(modal_id).innerHTML += modal_type
        else:
            modal_id = 'hookah_list'
            ordered_id = 'hookah_ordered'
            drinks_ordered = document.getElementById(ordered_id)
            if not drinks_ordered:
                modal_type = modal_segregate.replace('modal_type', 'Hookah')
                modal_type = modal_type.replace('ordered_id', ordered_id)
                document.getElementById(modal_id).innerHTML += modal_type

        render_html = modal_html.replace('item_name', order_item)
        render_html = render_html.replace('item_quantity', str(quantity))
        render_html = render_html.replace('individual_item_price', str(price))
        render_html = render_html.replace('total_item_price', str(total))
        document.getElementById(modal_id).innerHTML += render_html
    else:
        if parent_id == 'food_items':
            modal_id = 'food_list'
        elif parent_id == 'drinks_items':
            modal_id = 'drinks_list'
        else:
            modal_id = 'hookah_list'
        modal_body = document.getElementById(modal_id).getElementsByTagName('li')
        for ordered_item in modal_body:
            paras = ordered_item.getElementsByTagName('p')
            if order_item in paras[0].textContent:
                paras[1].textContent = quantity
                paras[-1].textContent = total


@when('click', '#preview_button')
def get_table_num():
    table_num = document.getElementById('table_number').value
    document.getElementById('modal_table_num').innerHTML = f"Table Number : {table_num}"
    amount_element = document.getElementById('total_amount').innerHTML
    document.getElementById('order_total').innerHTML = f"Order Total : {amount_element.split()[-1]}"