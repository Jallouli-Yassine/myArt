from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('welcome/', views.portal, name='portal'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
