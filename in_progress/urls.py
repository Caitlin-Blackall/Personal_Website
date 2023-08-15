from django.urls import path
from . import views

urlpatterns = [
    path('', views.in_progress, name='in_progress'),
]