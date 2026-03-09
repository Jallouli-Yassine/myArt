from django.shortcuts import render

def dashboard_home(request):
    return render(request, 'admin-dashboard.html')

def add_painting(request):
    return render(request, 'admin-add-painting.html')

def manage_paintings(request):
    return render(request, 'admin-paintings.html')

def manage_orders(request):
    return render(request, 'admin-orders.html')

def manage_users(request):
    return render(request, 'admin-users.html')
