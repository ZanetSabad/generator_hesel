
from django.contrib import admin
from django.urls import path
from generator import views



urlpatterns = [
    path('', views.home),
    path("kontakt", views.kontakt),
    path("cenik", views.cenik),
    path("sluzby", views.sluzby),
    path("password", views.password),
   
]
