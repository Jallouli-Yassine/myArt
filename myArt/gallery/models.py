from django.db import models
from django.contrib.auth.models import User

class Painting(models.Model):
    CATEGORY_CHOICES = (
        ('oil', 'Oil on Canvas'),
        ('watercolor', 'Watercolor'),
        ('acrylic', 'Acrylic'),
        ('digital', 'Digital Art'),
        ('mixed', 'Mixed Media'),
    )

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('sold', 'Sold'),
        ('reserved', 'Reserved'),
    )

    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='oil')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    image_path = models.CharField(max_length=500, blank=True, null=True, help_text="Enter image URL or path")
    likes = models.ManyToManyField(User, related_name='liked_paintings', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    painting = models.ForeignKey(Painting, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.painting.title}"
