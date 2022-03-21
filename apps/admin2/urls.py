from apps.admin2 import views
from django.urls import path

app_name = 'admin2'

urlpatterns = [
    path('user_list/', views.user_list, name='user_list'),
]
