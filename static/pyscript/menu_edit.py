import json
from pyweb import pydom

from pyscript import document, window, when
from js import WebSocket, console


initial_body = pydom['body'][0]

food_subcat = list(eval(pydom['#food_subcat'][0].html))
drinks_subcat = list(eval(pydom['#drinks_subcat'][0].html))
dessert_subcat = list(eval(pydom['#dessert_subcat'][0].html))

@when('click', '.edit-button')
def open_send_ws_data(event):
    target_id = event.target.getAttribute('id')
    slug_title = target_id.replace('button-', '')
    card_element = pydom[f'#raw-{slug_title}'][0]
    card_element.children[0].add_class('hidden')
    card_element.children[1].remove_class('hidden')
    


@when('click', '.save')
def send_form_data(event):
    slug_title = event.target.getAttribute('id').replace('save-', '')
    card_element = pydom[f'#raw-{slug_title}'][0]

    title = card_element.find('.title')[0].value
    card_element.find('.item-title')[0].html = title

    dish_image = card_element.find('.dish-image')[0].value
    card_element.find('.dish-image')[0].src = dish_image

    description = card_element.find('.description')[0].value
    card_element.find('.item-description')[0].html = description

    price = card_element.find('.price')[0].value
    card_element.find('.item-price')[0].html = price

    category = card_element.find('.category')[0].value
    card_element.find('.item-category')[0].html = category

    sub_category = card_element.find('.sub-category')[0].value
    card_element.find('.item-sub-category')[0].html = sub_category

    is_non_veg = card_element.find('.is-non-veg')[0].value
    card_element.find('.item-is-non-veg')[0].html = is_non_veg
    
    card_element.children[1].add_class('hidden')
    card_element.children[0].remove_class('hidden')

    # form_dict = {'title':title, 'dish_image':dish_image, 'description':description, 'price':price, 'category':category, 'sub_category':sub_category, 'is_non_veg':is_non_veg}
    # print(form_dict)
    # chat_socket = WebSocket.new(f'ws://{window.location.host}/ws/edit-menu/{slug_title}/')
    # chat_socket.onopen = lambda event: chat_socket.send(json.dumps({"message":slug_title}))
    # chat_socket.onmessage = lambda event: get_ws_data(event)
    

@when('click', '.back')
def back_to_card(event):
    slug_title = event.target.getAttribute('id').replace('back-', '')
    card_element = pydom[f'#raw-{slug_title}'][0]

    card_element.children[1].add_class('hidden')
    card_element.children[0].remove_class('hidden')



@when('change', '#id_category')
def subcat_condition():
    # if not pydom['#id_category'][0].options[0].value:
    #     pydom['#id_category'][0].options.remove(0)    

    subcat = pydom['#id_sub_category'][0]
    subcat.options.clear()
    category = pydom['#id_category'][0].options.selected.value
    if category == 'DRINKS':
        [subcat.options.add(value=value, html=text) for value, text in drinks_subcat]
    elif category == 'FOOD':
        [subcat.options.add(value=value, html=text) for value, text in food_subcat]
    elif category == 'DESSERT':
        [subcat.options.add(value=value, html=text) for value, text in dessert_subcat]


window.onload = subcat_condition()