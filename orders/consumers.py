from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

class OrderConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'order_{self.room_name}'

        'Join the order channel'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()


    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)