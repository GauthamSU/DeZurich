import json
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.template import Context, Template
from .models import OrderDetails, OrderItem
from static.pyscript.htmlstrings import order_html


class OrderConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'orders'

        'Join the order channel'
        await self.accept()
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
    
    
    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        message_type = text_data_json["type"]
        if message_type == 'order_id':
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "order.data", "message": message}
            )
        elif message_type == 'order_prepared':
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "order.prep.comp", "message": message}
            )

    async def order_data(self, event):
        order_id = event["message"]
        recent_order = await sync_to_async(OrderDetails.objects.get)(order_id=order_id)
        # recent_order_items = await sync_to_async(OrderItem.objects.filter)(order=recent_order)
        # for item in recent_order_items:
        #     item.product.category
        context = Context({"order":recent_order})
        template = Template(order_html)
        rendered_notification = await sync_to_async(template.render)(context)
        await self.send(text_data=json.dumps({"message": rendered_notification, "type":"order_card"}))


    async def order_prep_comp(self, event):
        order_id = event["message"]
        await self.send(text_data=json.dumps({"message": order_id, "type":"order_prep_comp"}))