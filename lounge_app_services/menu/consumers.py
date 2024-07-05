import json
from django import template
from lounge_app_services.custom_template_filters.templatetags import append_class
from .models import MenuItems
# from django.middleware import csrf
from .forms import EditMenuItemForm
from asgiref.sync import sync_to_async
from django.template import Context, Template, Engine
from static.pyscript.htmlstrings import edit_menu_form

from channels.generic.websocket import AsyncWebsocketConsumer


class EditMenuConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["slug_title"]
        self.room_group_name = f"chat_{self.room_name}"

        # 'Join the product edit channel'
        await self.accept()
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)


    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    
    async def receive(self, text_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        await self.channel_layer.group_send(
            self.room_group_name, {"type":"edit.menu" , "message": message}
        )


    async def edit_menu(self, event):
        slug_title = event['message']
        form_instance = await self.get_form_instance(slug_title)
        await self.send(text_data=json.dumps({'message':slug_title, 'form_instance':form_instance}))

    
    # @sync_to_async
    # def get_form_instance(self, slug_title):
    #     model_instances = MenuItems.objects.get(slug_title=slug_title)
    #     form_instances = [EditMenuItemForm(instance=instance) for instance in model_instances]
    #     # template = Template(edit_menu_form)
    #     # # csrf_token = csrf.get_token()
    #     # context = Context({'form':form_instance, 'slug_title':slug_title, 'csrf_token':csrf_token})
    #     # render_form = template.render(context)
    #     return form_instances