from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard'),
    path('add-painting/', views.add_painting, name='admin_add_painting'),
    path('paintings/', views.manage_paintings, name='admin_paintings'),
    path('orders/', views.manage_orders, name='admin_orders'),
    path('users/', views.manage_users, name='admin_users'),
]
