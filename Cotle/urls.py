from django.urls import path
from . import views

urlpatterns = [
    path('', views.rec_list, name='rec_list'),
    path('rec/<int:pk>/', views.rec_detail, name='rec_detail'),
    path('rec/new/', views.rec_new, name='rec_new'),
    ]

