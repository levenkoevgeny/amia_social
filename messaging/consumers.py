from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class MessageListenerConsumer(WebsocketConsumer):
    def connect(self):

        self.user = self.scope["user"]
        self.listener_name = 'listener_%s' % self.user.id

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.listener_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.listener_name,
            self.channel_name
        )

    def receive(self, text_data):
        pass

    def modal_message(self, event):
        print('here')
        self.send(text_data=event["text"])