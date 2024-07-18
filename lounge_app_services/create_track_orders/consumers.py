import json
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.template import Context, Template
from django.template.loader import render_to_string
from .models import OrderDetails
from lounge_app_services.menu.models import CATEGORY_CHOICES
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
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        message_type = text_data_json["type"]
        if message_type == 'order_id':
            send_type = "order.data"
        elif message_type == 'order_prepared':
            send_type = "order.prepared"
        elif message_type == 'order_served':
            send_type = "order.served"
            
        await self.channel_layer.group_send(
            self.room_group_name, {"type": send_type, "message": message}
        )


    async def order_data(self, event):
        order_id = event["message"]
        recent_order = await sync_to_async(OrderDetails.objects.get)(order_id=order_id)
        total_orders = await sync_to_async(OrderDetails.objects.filter)(order_placed__date=datetime.today().date())
        pending_orders = await sync_to_async(OrderDetails.objects.exclude)(order_status__in=['order_paid', 'order_completed'])
        context = {"order":recent_order, 'cat_choices':CATEGORY_CHOICES}
        kitchen_order_card_partial = 'create_track_orders/partials/track_order_partial.html#kitchen-order-card'
        rendered_notification = await sync_to_async(render_to_string)(kitchen_order_card_partial, context=context)
        total = await sync_to_async(len)(total_orders)
        pending = await sync_to_async(len)(pending_orders)
        await self.send(text_data=json.dumps({"message": rendered_notification, "type":"order_card", 'total_orders': total, 'pending_orders':pending}))


    async def order_prepared(self, event):
        order_id = event["message"]
        prepared_time = datetime.now()
        recent_order = await sync_to_async(OrderDetails.objects.get)(order_id=order_id)
        if recent_order.order_prepared:
            recent_order.order_prepared = None
            recent_order.order_status = 'order_placed'
        else:
            recent_order.order_prepared = prepared_time
            recent_order.order_status = 'order_prepared'
        await sync_to_async(recent_order.save)()
        await self.send(text_data=json.dumps({"message": order_id, "type":"order_prepared"}))

    
    async def order_served(self, event):
        order_id = event["message"]
        order = await sync_to_async(OrderDetails.objects.get)(order_id=order_id)
        order.order_status = 'order_completed'
        order.order_completed = datetime.now()
        if order.order_prepared:
            prepared ="true"
        else:
            prepared = "false"
        await sync_to_async(order.save)()
        await self.send(text_data=json.dumps({"message": order_id, "type":"order_served", "prepared":prepared}))
        
    # @sync_to_async
    # def update_order_status(self, order_id, prepared_time):
    #     order = OrderDetails.objects.get(order_id=order_id)
    #     order.order_status = 'order_completed'
    #     order.save()
