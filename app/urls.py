from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('user/signup', views.signup),
    path('user/signin', views.signin),
    path('user/profile', views.details),
    path('user/profile/update', views.update),
]
