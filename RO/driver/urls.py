from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="driver-home"),
    path('login/', views.driver_login, name="driver-login"),
    path('<int:driver_id>/', views.driver_detail, name='driver-detail')
]
