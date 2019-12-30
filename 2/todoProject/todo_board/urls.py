from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from .import views
from django.conf import settings
from django.conf.urls.static import static

# app_name = 'todo_board'

urlpatterns = [
    path('', views.todo_board, name='todo_board'),
    path('insert', views.check_post, name='todo_board_insert'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)