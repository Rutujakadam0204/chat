import json
from django.contrib.auth.models import User
from . models import MessageHistory, RoomNames
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        chatroom = await save_message_history(text_data, self.room_name)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))

from asgiref.sync import sync_to_async


@sync_to_async
def save_message_history(text_data,room_name):
    text_data = json.loads(text_data)
    room_name = RoomNames.objects.get(group_name=room_name)
    MessageHistory.objects.create(room=room_name, sender=User.objects.get(id=int(text_data['sender'])),text = text_data['message'])
    print(text_data)
    return


