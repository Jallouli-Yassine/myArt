from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Painting

def gallery_view(request):
    category = request.GET.get('category')
    if category:
        paintings = Painting.objects.filter(category=category)
    else:
        paintings = Painting.objects.all()
    
    categories = Painting.CATEGORY_CHOICES
    return render(request, 'gallery.html', {
        'paintings': paintings,
        'categories': categories,
        'selected_category': category
    })

def paintD_view(request, id):
    painting = get_object_or_404(Painting, id=id)
    return render(request, 'painting-detail.html', {'painting': painting})

@login_required(login_url='/accounts/login/') # Temporary fallback login page
def like_painting(request, id):
    painting = get_object_or_404(Painting, id=id)
    
    # Toggle like logic!
    if request.user in painting.likes.all():
        # User already liked it, so unlike it
        painting.likes.remove(request.user)
    else:
        # Give it a like
        painting.likes.add(request.user)
        
    referer = request.META.get('HTTP_REFERER')
    if referer:
        return redirect(referer)
    return redirect('paintD_view', id=id)

@login_required(login_url='/accounts/login/')
def add_comment(request, id):
    if request.method == 'POST':
        painting = get_object_or_404(Painting, id=id)
        body = request.POST.get('body')
        if body:
            from .models import Comment
            Comment.objects.create(painting=painting, user=request.user, body=body)
    return redirect('paintD_view', id=id)
