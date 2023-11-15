from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('login/', views.login, name='login'),
    path('user_login', views.user_login, name='user_login')
]