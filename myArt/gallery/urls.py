from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery_view, name='gallery'),
    path('details/<int:id>/', views.paintD_view, name='paintD_view'),
    path('like/<int:id>/', views.like_painting, name='like_painting'),
    path('comment/<int:id>/', views.add_comment, name='add_comment'),
]
