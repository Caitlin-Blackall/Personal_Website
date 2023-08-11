from django.urls import path
from . import views

urlpatterns = [
    path('', views.aws, name='aws'),
]