from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from main.views import ChangeLanguageView, IndexPageView,CHAT
from chatapp.views import chatPage

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexPageView.as_view(), name="index"),
    path("i18n/", include("django.conf.urls.i18n")),
    path("language/", ChangeLanguageView.as_view(), name="change_language"),
    path("accounts/", include("accounts.urls")),
    path('chat/<str:username>/', chatPage, name='chat'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
