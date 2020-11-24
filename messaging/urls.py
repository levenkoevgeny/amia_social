from django.urls import path
from . import views

app_name = 'messaging'

urlpatterns = [
    path('', views.messenger, name='messenger_main'),
]

