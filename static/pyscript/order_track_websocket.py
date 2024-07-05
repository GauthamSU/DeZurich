import asyncio
from datetime import datetime
from pyscript import document, window, when
import json
from js import WebSocket, console
# from pyodide.ffi.wrappers import add_event_listener

from pyweb import pydom

chat_socket = WebSocket.new(f'ws://{window.location.host}/ws/orders/')

chat_socket.onopen = lambda event: console.log('Websocket is open :', event)

if pydom['#message-data'][0].html:
    
    data_to_be_sent = pydom['#message-data'][0].html.replace('"', '')

    chat_socket.send(json.dumps({"message":data_to_be_sent, "type":"order_id"}))

    def receive_ws_data(event):
        message_data = json.loads(event.data)
        pydom['#render_data'][0].html += message_data['message']
        
    chat_socket.onmessage = lambda event: receive_ws_data(event)


@when('click', '#confirm-served')
def confirm_order_served(event):
    confirmation_text = pydom['#confirmation'][0]
    span_els = confirmation_text.find('span')
    order_id = span_els[0].html
    prepared_time = document.getElementById(f'prepared-{order_id}').dataset.preparedTime
    chat_socket.send(json.dumps({"message":order_id, "type":"order_served", "prepared_time":prepared_time}))


@when('click', '.order-prepared')
def send_ws_order_prepared(event):
    target_id = event.target.getAttribute('id')
    order_id = target_id.replace('prepared-', '')
    chat_socket.send(json.dumps({"message":order_id, "type":"order_prepared"}))


@when('click', '.order-served')
def update_modal_data(event):
    target_id = event.target.getAttribute('id')
    order_id = target_id.replace('served-', '')
    parent_element = pydom[f'#id-{order_id}']
    table_num = parent_element[0].find('.table-number')[0].html
    modal_display = pydom['#confirmation']
    span_els = modal_display[0].find('span')
    span_els[0].html = order_id
    span_els[1].html = table_num


def receive_set_order_prepared(order_id):
    # message_data = json.loads(event.data)
    # order_id = message_data['message']
    parent_element = pydom[f'#id-{order_id}']
    prepared_element = document.getElementById(f'prepared-{order_id}')
    initial_classes = ['bg-gradient-to-bl', 'from-orange-300', 'to-orange-100']
    if all(class_name in parent_element[0].classes for class_name in initial_classes): 
        parent_element[0].remove_class(initial_classes)
        parent_element[0].add_class('bg-green-800')
        prepared_element.dataset.preparedTime = str(datetime.now())
    else:
        parent_element[0].remove_class('bg-green-800')
        parent_element[0].add_class(initial_classes)
        prepared_element.dataset.preparedTime = ""


def receive_set_order_served(order_id):
    order_card = pydom[f'#id-{order_id}'][0]
    table_num = order_card.find('.table-number')[0].html
    confirm_html = f"""
    <div class="max-w-xs text-center bg-gradient-to-bl from-orange-300 to-orange-100 py-1 my-2 items-center">
        <div class="success-animation">
            <svg class="checkmark" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 52 52">
                <circle class="checkmark__circle" cx="26" cy="26" r="25" fill="none" />
                <path class="checkmark__check" fill="none" d="M14.1 27.2l7.1 7.2 16.7-16.8" />
            </svg>
        </div>
        <div class="top-1/2 left-auto">
            Order for table {table_num} with order Id {order_id} is completed.
        </div>
    </div>"""
    order_card.html = confirm_html


async def remove_order_card(order_id):
    order_card_js = document.getElementById(f'id-{order_id}')
    await asyncio.sleep(5)
    order_card_js.remove()


def get_set_event_data(event):
    event_data = json.loads(event.data)
    if event_data['type'] == 'order_prepared':
        receive_set_order_prepared(event_data['message'])
    elif event_data['type'] == 'order_served':
        receive_set_order_served(event_data['message'])
        asyncio.ensure_future(remove_order_card(event_data['message']))


chat_socket.onmessage = lambda event: get_set_event_data(event)

