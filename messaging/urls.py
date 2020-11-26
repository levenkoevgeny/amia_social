from django.urls import path
from . import views

app_name = 'messaging'

urlpatterns = [
    path('', views.messenger, name='messenger_main'),
    path('send_modal_message/', views.send_modal_message, name='send_modal_message'),
]

