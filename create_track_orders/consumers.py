import json
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.template import Context, Template
from .models import OrderDetails
from static.pyscript.htmlstrings import order_html
from datetime import datetime
from django.utils import timezone

class OrderConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'orders'

        'Join the order channel'
        await self.accept()
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
    
    
    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        time = ''
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        message_type = text_data_json["type"]
        if message_type == 'order_id':
            send_type = "order.data"
        elif message_type == 'order_prepared':
            send_type = "order.prepared"
        elif message_type == 'order_served':
            send_type = "order.served"
            time = text_data_json['prepared_time']
        
        await self.channel_layer.group_send(
            self.room_group_name, {"type": send_type, "message": message, 'time':time}
        )

    async def order_data(self, event):
        order_id = event["message"]
        recent_order = await sync_to_async(OrderDetails.objects.get)(order_id=order_id)
        context = Context({"order":recent_order})
        template = Template(order_html)
        rendered_notification = await sync_to_async(template.render)(context)
        await self.send(text_data=json.dumps({"message": rendered_notification, "type":"order_card"}))


    async def order_prepared(self, event):
        order_id = event["message"]
        await self.send(text_data=json.dumps({"message": order_id, "type":"order_prepared"}))

    
    async def order_served(self, event):
        order_id = event["message"]
        prepared_time = event['time']
        await self.send(text_data=json.dumps({"message": order_id, "type":"order_served"}))
        await self.update_order_status(order_id, prepared_time)

    @sync_to_async
    def update_order_status(self, order_id, prepared_time):
        order = OrderDetails.objects.get(order_id=order_id)
        order.order_status = 'order_completed'
        if prepared_time != '':
            date_format = "%Y-%m-%d %H:%M:%S.%f"
            date_object = datetime.strptime(prepared_time, date_format)
            order.order_prepared = date_object
        order.save()
