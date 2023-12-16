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


@when('click', '.order-prepared')
def send_ws_order_prepared(event):
    target_id = event.target.getAttribute('id')
    order_id = target_id.replace('prepared-', '')
    chat_socket.send(json.dumps({"message":order_id, "type":"order_prepared"}))


def receive_set_order_prepared(order_id):
    # message_data = json.loads(event.data)
    # order_id = message_data['message']
    parent_element = pydom[f'#id-{order_id}']
    table_num = parent_element[0].find('.table-number')
    initial_classes = ['bg-gradient-to-bl', 'from-orange-300', 'to-orange-100']
    if all(class_name in parent_element[0].classes for class_name in initial_classes): 
        parent_element[0].remove_class(initial_classes)
        parent_element[0].add_class('bg-green-800')
    else:
        parent_element[0].remove_class('bg-green-800')
        parent_element[0].add_class(initial_classes)


def get_set_event_data(event):
    event_data = json.loads(event.data)
    if event_data['type'] == 'order_prep_comp':
        receive_set_order_prepared(event_data['message'])

chat_socket.onmessage = lambda event: get_set_event_data(event)

