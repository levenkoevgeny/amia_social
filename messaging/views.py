from channels.layers import get_channel_layer
from django.shortcuts import render


def messenger(request):
    return render(request, 'messaging/messenger.html')


def send_modal_message(request):
    print(request.POST)
    message_text = request.POST['message']

    channel_layer = get_channel_layer()
    channel_layer.send("channel_name", {
        "type": "modal.message",
        "text": message_text,
    })

