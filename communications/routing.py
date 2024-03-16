from django.urls import path
from . import consumers
websocket_urlpatterns = [
    path('ws/chat/<username_from>/<username_to>/', consumers.CommunicationsConsumer.as_asgi()),
]