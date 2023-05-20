from django.contrib import admin
from django.urls import path
from Home import views


urlpatterns = [
    path('', views.index, name='Home'),
    path('analysis', views.analysis, name='Analysis'),
    path('customer', views.customer, name='Customer'),
    path('submit', views.submit, name='Submit')
]