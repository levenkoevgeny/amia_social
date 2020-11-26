import json
from channels.generic.websocket import WebsocketConsumer
from .models import Clients


class MessageListenerConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        Clients.objects.create(client=self.scope["user"], channels_name=self.channel_name)

        print(self.channel_name)

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        pass

    def modal_message(self, event):
        self.send(text_data=event["message"])