from pyscript import window, when, display
import js
from js import document, Cookies

# pyodide_http.patch_all()

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
        <span class="px-10 py-0\.5 text-center text-gray-700 bg-gray-100 border border-gray-200 rounded-lg dark:border-gray-500 dark:text-gray-100 dark:bg-gray-400 preference_target">customer_preference</span>
    </div>
</li>
"""

data_dict = {}

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


@when('click', '.minus')
def reduce(event):
    ele = event.target
    quantity_name = ele.getAttribute('id')
    slug_name = quantity_name.replace('minus-', '')
    quantity_element = document.getElementById(f'quantity-{slug_name}')
    quantity = int(quantity_element.value)
    if quantity > 0:
        quantity -= 1
        quantity_element.value = quantity
        if quantity == 0:
            document.getElementById(slug_name).getElementsByClassName('preference')[0].disabled = True
            preference_input = document.getElementById(slug_name).getElementsByClassName('preference_input')[0]
            if not 'hidden' in preference_input.classList:
                preference_input.classList.add('hidden')

        update_total(slug_name, 'minus')
        get_preview_details(slug_name, quantity)


@when('click', '.plus')
def increase(event):
    ele = event.target
    quantity_name = ele.getAttribute('id')
    slug_name = quantity_name.replace('plus-', '')
    quantity_element = document.getElementById(f'quantity-{slug_name}')
    quantity = int(quantity_element.value)
    quantity += 1
    quantity_element.value = quantity
    document.getElementById(slug_name).getElementsByClassName('preference')[0].disabled = False
    preference_input = document.getElementById(slug_name).getElementsByClassName('preference_input')[0]
    if not 'hidden' in preference_input.classList:
        preference_input.classList.remove('hidden')
    update_total(slug_name, 'plus')
    get_preview_details(slug_name, quantity)


@when('click', '.preference')
def show_preference_input(event):
    target_element = event.target
    preference_id = target_element.getAttribute('id')
    slug_name = preference_id.replace('preference-', '')
    quantity = document.getElementById(f'quantity-{slug_name}').value
    hidden_element = document.getElementById(slug_name).getElementsByClassName('preference_input')[0]
    if int(quantity) > 0:
        if 'hidden' in hidden_element.classList:
            hidden_element.classList.remove('hidden')
        else:
            hidden_element.classList.add('hidden')


@when('click', '#preview_button')
def get_table_num():
    food_html_list = """<p class="dark:text-white text-gray-900 text-lg font-medium" id="food_ordered">Foods Ordered: </p>"""
    drinks_html_list = """<p class="dark:text-white text-gray-900 text-lg font-medium" id="drinks_ordered">Drinks Ordered: </p>"""
    hookah_html_list = """<p class="dark:text-white text-gray-900 text-lg font-medium" id="hookah_ordered">Hookah Ordered: </p>"""
    table_num = document.getElementById('table_number').value
    document.getElementById('modal_table_num').innerHTML = f"Table Number : {table_num}"
    amount_element = document.getElementById('total_amount').innerHTML
    document.getElementById('order_total').innerHTML = f"Order Total : {amount_element.split()[-1]}"
    for item, data in data_dict.items():
        if data[2] > 0 :
            render_html = modal_html.replace('slugified_name', f'preview-{item}')
            render_html = modal_html.replace('item_name', data[0])
            render_html = render_html.replace('item_quantity', str(data[2]))
            render_html = render_html.replace('individual_item_price', str(data[3]))
            render_html = render_html.replace('total_item_price', str(round(float(data[2]*data[3]), 3)))
            if data[4] != '':
                render_html = render_html.replace('customer_preference', data[4])
                render_html = render_html.replace('hidden', '')
            else:
                if not 'hidden' in render_html:
                    render_html = render_html.replace('<div class="p-1 px-2', '<div class="p-1 px-2 hidden')
            if data[1] == 'food_items':
                food_html_list += render_html
            elif data[1] == 'drinks_items':
                drinks_html_list += render_html
            else:
                hookah_html_list += render_html

    document.getElementById('food_list').innerHTML = (food_html_list)
    document.getElementById('drinks_list').innerHTML = (drinks_html_list)
    document.getElementById('hookah_list').innerHTML = (hookah_html_list)


@when('change', '.preference_input')
def add_preference_to_modal(event):
    target_element = event.target
    preference_id = target_element.getAttribute('id')
    slug_name = preference_id.replace('preference-', '')
    quantity = int(document.getElementById(f'quantity-{slug_name}').value)
    preference = target_element.value
    get_preview_details(slug_name, quantity, preference)


def update_total(slug_name, operator):
    amount_value = document.getElementById('total_amount').innerHTML
    quantity_value = document.getElementById('num_items').innerHTML
    # quantity = document.getElementById(f'quantity-{slug_name}').value
    amount = document.getElementById(f'price-{slug_name}').innerHTML

    if operator == 'plus':
        total_quantity = int(quantity_value) +  1
        total_amount = float(amount) + float(amount_value)
    else:
        total_quantity = int(quantity_value) - 1
        total_amount = float(amount_value) - float(amount)

    document.getElementById('num_items').innerHTML = round(total_quantity, 2)
    document.getElementById('total_amount').innerHTML = round(total_amount, 2)

    document.getElementsByName('total-items')[0].value = round(total_quantity, 2)
    document.getElementsByName('total-amount')[0].value = round(total_amount, 2)


def get_preview_details(slug_name, quantity, preference=''):
    product_item = document.getElementById(slug_name).getElementsByClassName('menu-item')[0].textContent
    product_type = document.getElementById(slug_name).parentNode.getAttribute('id')
    price = float(document.getElementById(f'price-{slug_name}').textContent)
    if (slug_name in data_dict) and data_dict[slug_name][4] != '':
        preference = data_dict[slug_name][4]
    data_dict[slug_name] = [product_item.strip(), product_type, quantity, price, preference]
    


# @when('click', '#submit_botton')
# def send_request():
#     csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0].value
#     complete_url = window.location.href
#     new_url = f'{window.location.hostname}/internal/order/track-order/'
#     requests.post(url=complete_url, data=data_dict, headers={'X-CSRFToken': csrftoken, 'Location':new_url})
#     # requests.post(url=complete_url, json=json.dumps(data_dict), headers={'Content-Type': 'application/json','X-CSRFToken': csrftoken})