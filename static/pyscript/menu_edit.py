import json
from pyweb import pydom

from pyscript import document, window, when
from js import WebSocket, console


def get_subcats():
    food_subcat = list(eval(pydom['#food_subcat'][0].html))
    drinks_subcat = list(eval(pydom['#drinks_subcat'][0].html))
    dessert_subcat = list(eval(pydom['#dessert_subcat'][0].html))
    return food_subcat, drinks_subcat, dessert_subcat


@when('change', '#id_category')
def filter_subcat_condition():
    
    food_subcat, drinks_subcat, dessert_subcat = get_subcats()

    subcat = pydom['#id_sub_category'][0]
    subcat.options.clear()
    category = pydom['#id_category'][0].options.selected.value
    if category == 'DRINKS':
        [subcat.options.add(value=value, html=text) for value, text in drinks_subcat]
    elif category == 'FOOD':
        [subcat.options.add(value=value, html=text) for value, text in food_subcat]
    elif category == 'DESSERT':
        [subcat.options.add(value=value, html=text) for value, text in dessert_subcat]
    else:
        subcat.options.add(value="Hookah", html="Hookah")

window.onload = filter_subcat_condition()

@when('change', '.category')
def form_subcat_condition(event, slug_title=None):
    
    food_subcat, drinks_subcat, dessert_subcat = get_subcats()

    if not slug_title:
        item_category_id = event.target.getAttribute('id')
    else:
        item_category_id = f"id_{slug_title}_category"

    item_sub_category_id = item_category_id.replace('category', 'sub_category')
    category = pydom[f'#{item_category_id}'][0].options.selected.value
    sub_category = pydom[f'#{item_sub_category_id}'][0].options.selected.value
    subcat = pydom[f'#{item_sub_category_id}'][0]
    subcat.options.clear()

    if category == 'DRINKS':
        [subcat.options.add(value=value, html=text) for value, text in drinks_subcat]
        [option._js.setAttribute('selected', 'true') for option in subcat.options if option.value == sub_category]
    elif category == 'FOOD':
        [subcat.options.add(value=value, html=text) for value, text in food_subcat]
        [option._js.setAttribute('selected', 'true') for option in subcat.options if option.value == sub_category]
    elif category == 'DESSERT':
        [subcat.options.add(value=value, html=text) for value, text in dessert_subcat]
        [option._js.setAttribute('selected', 'true') for option in subcat.options if option.value == sub_category]
    else:
        subcat.options.add(value="Hookah", html="Hookah")


@when('htmx:afterSwap', '.w-full')
def initial_swap_subcats(event):
    item_category_id = event.target.getAttribute('id')
    if item_category_id and 'form-wrapper' in event.target.classList:
        slug_title = item_category_id.replace('id-form-', '')
        form_subcat_condition(event, slug_title)


@when('htmx:afterSwap', '#menu-edit-filter-page')
def after_filter_swap(event):
    for child in pydom['#filtered-data'][0].children:
        for grand_child in child.children:
            if grand_child._js.tagName == 'DIV' and 'grid' in grand_child.classes:
                if not len(grand_child.children):
                    child.remove_class('block')
                    child.add_class('hidden')
    
