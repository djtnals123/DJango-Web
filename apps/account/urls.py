from apps.account import views
from django.urls import path

app_name = 'account'

urlpatterns = [
    path('agree/', views.agree, name='agree'),
    path('register/', views.register, name='register'),
    path('modify/', views.modify, name='modify')
]
