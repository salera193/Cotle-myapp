from django.urls import path
from . import views

urlpatterns = [
    path('', views.rec_list, name='rec_list'),
    path('rec/<int:pk>/', views.rec_detail, name='rec_detail'),
    path('rec/new/', views.rec_new, name='rec_new'),
    path('app/new/<int:pk>/', views.app_new, name='app_new'),
    path('app/del/<int:pk>/', views.app_del, name='app_del'),
    path('rec/acc/<int:pk>/<int:rpk>/', views.acc_app, name='acc_app'),
    path('rec/acc/cancel/<int:pk>/<int:rpk>/', views.acc_cancel, name='acc_cancel'),
    ]

