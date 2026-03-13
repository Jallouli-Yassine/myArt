from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.contrib import messages

from gallery.models import Painting

@staff_member_required(login_url='/accounts/login/')
def dashboard_home(request):
    return render(request, 'admin-dashboard.html')

@staff_member_required(login_url='/accounts/login/')
def manage_paintings(request):
    paintings = Painting.objects.all()
    # just plain all and order by id desc
    paintings = Painting.objects.all().order_by('-id')
    return render(request, 'admin-paintings.html', {'paintings': paintings})

@staff_member_required(login_url='/accounts/login/')
def add_painting(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description')
        category = request.POST.get('category')
        status = request.POST.get('status')
        
        image_path = None
        if 'image' in request.FILES:
            from django.core.files.storage import default_storage
            uploaded_file = request.FILES['image']
            filename = default_storage.save(f"paintings/{uploaded_file.name}", uploaded_file)
            image_path = default_storage.url(filename)
        else:
            image_path = request.POST.get('image')

        Painting.objects.create(
            title=title,
            price=price,
            description=description,
            category=category,
            status=status,
            image_path=image_path
        )
        messages.success(request, 'Painting added successfully!')
        return redirect('admin_paintings')

    return render(request, 'admin-add-painting.html')

@staff_member_required(login_url='/accounts/login/')
def edit_painting(request, id):
    painting = get_object_or_404(Painting, id=id)
    if request.method == 'POST':
        painting.title = request.POST.get('title')
        painting.price = request.POST.get('price')
        painting.description = request.POST.get('description')
        painting.category = request.POST.get('category')
        painting.status = request.POST.get('status')
        
        if 'image' in request.FILES:
            from django.core.files.storage import default_storage
            uploaded_file = request.FILES['image']
            filename = default_storage.save(f"paintings/{uploaded_file.name}", uploaded_file)
            painting.image_path = default_storage.url(filename)
        elif request.POST.get('image'):
             painting.image_path = request.POST.get('image')

        painting.save()
        messages.success(request, 'Painting updated successfully!')
        return redirect('admin_paintings')

    return render(request, 'admin-edit-painting.html', {'painting': painting})

@staff_member_required(login_url='/accounts/login/')
def delete_painting(request, id):
    painting = get_object_or_404(Painting, id=id)
    painting.delete()
    messages.success(request, 'Painting deleted successfully!')
    return redirect('admin_paintings')

@staff_member_required(login_url='/accounts/login/')
def manage_orders(request):
    return render(request, 'admin-orders.html')

@staff_member_required(login_url='/accounts/login/')
def manage_users(request):
    users = User.objects.all().order_by('-date_joined')
    return render(request, 'admin-users.html', {'users': users})

@staff_member_required(login_url='/accounts/login/')
def delete_user(request, id):
    user_obj = get_object_or_404(User, id=id)
    if not user_obj.is_superuser: # protect superusers from being deleted easily
        user_obj.delete()
        messages.success(request, 'User deleted successfully!')
    else:
        messages.error(request, 'Cannot delete a superuser from this dashboard!')
    return redirect('admin_users')

@staff_member_required(login_url='/accounts/login/')
def toggle_admin(request, id):
    user_obj = get_object_or_404(User, id=id)
    if not user_obj.is_superuser: # Prevent demoting the superuser accidentally
        user_obj.is_staff = not user_obj.is_staff
        user_obj.save()
        status = "promoted to Admin" if user_obj.is_staff else "demoted to User"
        messages.success(request, f'User {status} successfully!')
    else:
        messages.error(request, 'Cannot change superuser permissions from here!')
    return redirect('admin_users')

