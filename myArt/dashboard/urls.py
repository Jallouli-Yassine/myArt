from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard'),
    path('add-painting/', views.add_painting, name='admin_add_painting'),
    path('edit-painting/<int:id>/', views.edit_painting, name='admin_edit_painting'),
    path('delete-painting/<int:id>/', views.delete_painting, name='admin_delete_painting'),
    path('paintings/', views.manage_paintings, name='admin_paintings'),
    
    path('orders/', views.manage_orders, name='admin_orders'),
    
    path('users/', views.manage_users, name='admin_users'),
    path('delete-user/<int:id>/', views.delete_user, name='admin_delete_user'),
    path('toggle-admin/<int:id>/', views.toggle_admin, name='admin_toggle_admin'),
]
