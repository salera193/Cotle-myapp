from django.urls import path
from . import views

urlpatterns = [
    path('', views.rec_list, name='rec_list'),
    ]

