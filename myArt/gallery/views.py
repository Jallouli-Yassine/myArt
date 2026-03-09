from django.shortcuts import render

def gallery_view(request):
    return render(request, 'gallery.html')

def paintD_view(request, id):
    # For now, we'll just pass the ID so the template renders
    # Later, you will query the database: Painting.objects.get(id=id)
    return render(request, 'painting-detail.html', {'painting_id': id})
