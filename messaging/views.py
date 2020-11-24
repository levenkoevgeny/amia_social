from django.shortcuts import render


def messenger(request):
    return render(request, 'messaging/messenger.html')
