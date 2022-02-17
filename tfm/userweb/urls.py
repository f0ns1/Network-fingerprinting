from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('scan', views.scan, name='scan'),
    path('reports', views.reports, name='reports')
]