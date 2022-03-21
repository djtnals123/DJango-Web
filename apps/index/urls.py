from django.urls import path, include
from apps.index import views
from django.contrib.auth import views as auth_views

app_name = 'index'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login_form.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('choose_function/', views.choose_function, name='choose_function')
]
