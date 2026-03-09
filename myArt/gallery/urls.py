from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery_view, name='gallery'),
    path('details/<int:id>/', views.paintD_view, name='paintD_view'),
]
