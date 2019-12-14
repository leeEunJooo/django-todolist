from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from .import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'todo_main'

urlpatterns = [
    path('', views.Todo_main, name='todo_main'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)