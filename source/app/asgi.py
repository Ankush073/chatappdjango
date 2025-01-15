import os

from django.core.asgi import get_asgi_application

from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter

from channels.auth import AuthMiddlewareStack

from chatapp.consumers import PersonalChatConsumer, OnlineStatusConsumer, NotificationConsumer
# print("DJANGO_SETTINGS_MODULE")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_asgi_application()


application = ProtocolTypeRouter({
    "http":application,
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws/<int:id>/', PersonalChatConsumer.as_asgi()),
            path('ws/online/', OnlineStatusConsumer.as_asgi()),
            path('ws/notify/', NotificationConsumer.as_asgi())
        ])
    )
})