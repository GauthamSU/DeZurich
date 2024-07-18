import asyncio
from datetime import datetime
from pyscript import document, window, when
import json
from js import WebSocket, console
from time import sleep

from pyweb import pydom

chat_socket = WebSocket.new(f'ws://{window.location.host}/ws/orders/')


def send_created_order(event, chat_socket):
    if pydom['#message-data'][0].html:
        data_to_be_sent = pydom['#message-data'][0].html.replace('"', '')
        chat_socket.send(json.dumps({"message":data_to_be_sent, "type":"order_id"}))


chat_socket.onopen = lambda event: send_created_order(event, chat_socket)
    

@when('click', '#confirm-served')
def confirm_order_served(event):
    confirmation_text = pydom['#served-confirmation'][0]
    span_els = confirmation_text.find('span')
    order_id = span_els[0].html
    chat_socket.send(json.dumps({"message":order_id, "type":"order_served"}))


@when('click', '#confirm-prepared')
def send_ws_order_prepared(event):
    confirmation_text = pydom['#prepared-confirmation'][0]
    span_els = confirmation_text.find('span')
    order_id = span_els[0].html
    chat_socket.send(json.dumps({"message":order_id, "type":"order_prepared"}))


@when('click', '.order-prepared')
def update_prepared_modal(event):
    if event.target.tagName == 'BUTTON':
        target_id = event.target.children[0].getAttribute('id')
    else:
        target_id = event.target.getAttribute('id')
    order_id = target_id.replace('prepared-', '')
    parent_element = pydom[f'#id-{order_id}']
    table_num = parent_element[0].find('.table-number')[0].html
    modal_display = pydom['#prepared-confirmation']
    span_els = modal_display[0].find('span')
    span_els[0].html = order_id
    span_els[1].html = table_num


@when('click', '.order-served')
def update_modal_data(event):
    if event.target.tagName == 'BUTTON':
        target_id = event.target.children[0].getAttribute('id')
    else:
        target_id = event.target.getAttribute('id')
    order_id = target_id.replace('served-', '')
    parent_element = pydom[f'#id-{order_id}']
    table_num = parent_element[0].find('.table-number')[0].html
    modal_display = pydom['#served-confirmation']
    span_els = modal_display[0].find('span')
    span_els[0].html = order_id
    span_els[1].html = table_num


def receive_set_order_prepared(order_id):
    # message_data = json.loads(event.data)
    # order_id = message_data['message']
    parent_element = pydom[f'#id-{order_id}'][0]
    
    initial_classes = ['bg-gradient-to-bl', 'from-orange-700', 'to-orange-400']
    prepared_classes = ['bg-gradient-to-bl', 'from-green-600', 'to-green-300']
    if all(class_name in parent_element.classes for class_name in initial_classes): 
        parent_element.remove_class(initial_classes)
        parent_element.add_class(prepared_classes)
    else:
        parent_element.remove_class(prepared_classes)
        parent_element.add_class(initial_classes)
        

def receive_ws_data(message, total_orders, pending_orders):
    if not pydom['#message-data'][0].html:
        pydom['#render_data'][0].html = message + pydom['#render_data'][0].html

    pydom['#total-tables-served'][0].html = str(total_orders)
    pydom['#pending-tables'][0].html = str(pending_orders)


def receive_set_order_served(order_id, prepared):
    order_card = pydom[f'#id-{order_id}'][0]
    table_num = order_card.find('.table-number')[0].html
    if prepared == "true":
        classes = "bg-gradient-to-bl from-green-600 to-green-300"
    else:
        classes = "bg-gradient-to-bl from-orange-700 to-orange-400"
    confirm_html = f"""
        <div class="success-animation flex flex-col justify-center gap-4">
            <svg class="checkmark" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 52 52">
                <circle class="checkmark__circle" cx="26" cy="26" r="25" fill="none" />
                <path class="checkmark__check" fill="none" d="M14.1 27.2l7.1 7.2 16.7-16.8" />
            </svg>
            <div class="items-start px-5">
                Order for table {table_num} with order Id {order_id} is completed.
            </div>
        </div>
        """
    order_card.html = confirm_html


async def remove_order_card(order_id):
    order_card_js = pydom[f'#id-{order_id}'][0]
    await asyncio.sleep(3)
    order_card_js._js.remove()


def get_set_event_data(event):
    
    event_data = json.loads(event.data)

    if event_data['type'] == 'order_prepared':
        receive_set_order_prepared(event_data['message'])
    elif event_data['type'] == 'order_card':
        message = event_data['message']
        total_orders = event_data['total_orders']
        pending_orders = event_data['pending_orders']
        receive_ws_data(message, total_orders, pending_orders)
    elif event_data['type'] == 'order_served':
        receive_set_order_served(event_data['message'], event_data['prepared'])
        asyncio.ensure_future(remove_order_card(event_data['message']))


chat_socket.onmessage = lambda event: get_set_event_data(event)

