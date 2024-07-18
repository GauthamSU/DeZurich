from pyscript import window, when, display
import json
from pyweb import pydom
from pyodide.ffi.wrappers import add_event_listener


table_num = pydom['#table_number'][0].value
if int(table_num) == 0:
    pydom['#preview_button'][0]._js.disabled = True


@when('change', '#table_number')
def change_disable():
    table_num = pydom['#table_number'][0].value
    num_items = pydom['#num_items'][0].html
    popover = pydom['#popover-top'][0].children[0]
    if int(table_num) == 0:
        pydom['#preview_button'][0]._js.disabled = True
        popover.html = "<p>Please enter the table number for the Order.</p>"
    elif int(num_items) == 0:
        pydom['#preview_button'][0]._js.disabled = True
        popover.html = "<p>Please place an order to preview the order list.</p>"
    else:
        pydom['#preview_button'][0]._js.disabled = False
        pydom['#popover-top'][0].add_class('hidden')


@when('click', '.minus')
def reduce(event):
    ele = event.target
    quantity_name = ele.getAttribute('id')
    slug_name = quantity_name.replace('minus-', '')
    quantity_element = pydom[f'#quantity-{slug_name}'][0]
    quantity = int(quantity_element.value)
    if quantity > 0:
        quantity -= 1
        quantity_element.value = quantity
        if quantity == 0:
            pydom[f"#id-{slug_name}"][0].find('.preference')[0]._js.disabled = True
            preference_input = pydom[f"#id-{slug_name}"][0].find('.preference_input')[0]
            if not 'hidden' in preference_input.classes:
                preference_input.add_class('hidden')
            if 'hidden' in pydom['#popover-top'][0].classes:    
                pydom['#popover-top'][0].remove_class('hidden')
                pydom['#preview_button'][0]._js.disabled = True
        
        update_total(slug_name, 'minus')

        

@when('click', '.plus')
def increase(event):
    ele = event.target
    quantity_name = ele.getAttribute('id')
    slug_name = quantity_name.replace('plus-', '')
    quantity_element = pydom[f'#quantity-{slug_name}'][0]
    quantity = int(quantity_element.value)
    quantity += 1
    quantity_element.value = quantity
    pydom[f"#id-{slug_name}"][0].find('.preference')[0]._js.disabled = False
    preference_input = pydom[f"#id-{slug_name}"][0].find('.preference_input')[0]
    if not 'hidden' in preference_input.classes:
        preference_input.remove_class('hidden')
    if not 'hidden' in pydom['#popover-top'][0].classes and int(pydom['#table_number'][0].value) > 0:    
        pydom['#popover-top'][0].add_class('hidden')
        pydom['#preview_button'][0]._js.disabled = False
    
    update_total(slug_name, 'plus')

    

@when('click', '.preference')
def show_preference_input(event):
    target_element = event.target
    preference_id = target_element.getAttribute('id')
    slug_name = preference_id.replace('preference-', '')
    quantity = pydom[f'#quantity-{slug_name}'][0]
    hidden_element = pydom[f"#id-{slug_name}"][0].find('.preference_input')[0]
    if int(quantity.value) > 0:
        if 'hidden' in hidden_element.classes:
            hidden_element.remove_class('hidden')
        else:
            hidden_element.add_class('hidden')


def update_total(slug_name, operator):
    amount_value = pydom['#total_amount'][0].html
    quantity_value = pydom['#num_items'][0].html
    amount = pydom[f'#price-{slug_name}'][0].html

    if operator == 'plus':
        total_quantity = int(quantity_value) +  1
        total_amount = float(amount) + float(amount_value)
    else:
        total_quantity = int(quantity_value) - 1
        total_amount = float(amount_value) - float(amount)

    pydom['#num_items'][0].html = round(total_quantity, 2)
    pydom['#total_amount'][0].html = round(total_amount, 2)

    pydom["[name='total-items']"][0].value = round(total_quantity, 2)
    pydom["[name='total-amount']"][0].value = round(total_amount, 2)



@when('click', '#food_drop_down')
@when('click', '#drinks_drop_down')
@when('click', '#hookah_drop_down')
def show_dropdown_list(event):
    target_tag_name = event.target.tagName 
    if target_tag_name == 'DIV':
        target_id = event.target.getAttribute('id')
    elif target_tag_name == 'H4' or target_tag_name == 'SPAN':
        target_id = event.target.parentNode.getAttribute('id')
    elif target_tag_name == 'svg':
        target_id = event.target.parentNode.parentNode.getAttribute('id')
    else:
        target_id = event.target.parentNode.parentNode.parentNode.getAttribute('id')

    svg_span = pydom[f'#{target_id}'][0].find('svg')[0]
    classes = ['rotate-180', 'ease-in-out', 'transition-transform']
    category = target_id.split('_')[0]
    if all(cls in svg_span.classes for cls in classes):
        svg_span.remove_class('rotate-180')
        svg_span.add_class('-rotate-180')

        pydom[f'#{category}-filter-form'][0].remove_class('flex')
        pydom[f'#{category}-filter-form'][0].add_class('hidden')

        pydom[f'#{category}-items-list'][0].remove_class('block')
        pydom[f'#{category}-items-list'][0].add_class('hidden')
    else:
        svg_span.add_class(classes)

        pydom[f'#{category}-filter-form'][0].remove_class('hidden')
        pydom[f'#{category}-filter-form'][0].add_class('flex')

        pydom[f'#{category}-items-list'][0].remove_class('hidden')
        pydom[f'#{category}-items-list'][0].add_class('block')


@when('htmx:afterSwap', '#food-items-list')
@when('htmx:afterSwap', '#drinks-items-list')
@when('htmx:afterSwap', '#hookah-items-list')
def attach_event_listeners(event):
    swapped_id = event.target.getAttribute('id')
    minus = pydom[f'#{swapped_id}'][0].find('.minus')
    plus = pydom[f'#{swapped_id}'][0].find('.plus')
    preference = pydom[f'#{swapped_id}'][0].find('.preference')
    
    if minus:
        for el in minus:
            add_event_listener(el._js, 'click', reduce)

        for el in plus:
            add_event_listener(el._js, 'click', increase)

        for el in preference:
            add_event_listener(el._js, 'click', show_preference_input)



@when('htmx:afterSwap', '#filtered-json-data')
def get_filtered_json(event):
    filtered_data = pydom['#filtered-json-data'][0].html
    json_data = json.loads(filtered_data)
    queryset = json_data['order_filter_queryset']
    excluded = json_data['excluded_queryset']
    
    for item in excluded:
        slug_title = item['slug_title']
        card_element = pydom[f'#id-{slug_title}'][0]
        if not 'hidden' in card_element.classes:
            card_element.add_class('hidden')
    
    for item in queryset:
        slug_title = item['slug_title']
        card_element = pydom[f'#id-{slug_title}'][0]
        if 'hidden' in card_element.classes:
            card_element.remove_class('hidden')