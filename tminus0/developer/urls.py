from django.contrib import admin
from django.urls import path
from developer import views

urlpatterns = [
    path("", views.index)
]
