from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('main.urls', namespace="main")),
    path('admin/', admin.site.urls),
]

if settings.DEBUG