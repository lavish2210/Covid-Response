from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkup, name='checkup'),
    path('askpin', views.askpin, name='askpin'),
]