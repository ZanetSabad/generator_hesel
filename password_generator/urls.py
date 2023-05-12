
from django.contrib import admin
from django.urls import path
from generator import views
from django.urls import path, include


urlpatterns = [
    path('', views.home),
    path("kontakt", views.kontakt),
    path("cenik", views.cenik),
    path("sluzby", views.sluzby),
    path("password", views.password),
    path('', include('password_generator.urls')),
]
