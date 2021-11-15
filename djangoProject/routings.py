from django.urls import re_path

from phc import consumers

websocket_urlpatterns = [
    re_path(r'chatchannel/(?P<group>\w+)/$',consumers.ChatConsumer.as_asgi()),
]