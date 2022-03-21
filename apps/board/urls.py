from apps.board import views
from django.urls import path

app_name = 'board'

urlpatterns = [
    path('list/', views.list, name='list'),
    path('write/', views.write, name='write'),
    path('modify/<int:board_id>/', views.modify, name='modify'),
    path('read/<int:board_id>/', views.read, name='read'),
    path('delete/<int:board_id>/', views.delete, name='delete'),
]
