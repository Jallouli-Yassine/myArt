"""myArt URL Configuration"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # Standard Django Admin perfectly restored
    path('', include('pages.urls')), # Home, About, Contact
    path('gallery/', include('gallery.urls')), # Gallery, Painting Details      
    path('accounts/', include('accounts.urls')), # Login, Register, Profile     
    path('shop/', include('shop.urls')), # Shop views
    path('dashboard/', include('dashboard.urls')), # Custom admin pages
]
