from django.db import models

class ImagePost(models.Model):
    CATEGORY_CHOICES = [
        ('Nature', 'Nature'),
        ('Travel', 'Travel'),
        ('Food', 'Food'),
        ('Art', 'Art'),
        ('Lifestyle', 'Lifestyle'),
        ('Technology', 'Technology'),
        ('Architecture', 'Architecture'),
        ('Fashion', 'Fashion'),
        ('Sports', 'Sports'),
        ('Animals', 'Animals'),
        ('People', 'People'),
        ('Events', 'Events'),
        ('Business', 'Business'),
        ('Other', 'Other'),
    ]

    title = models.CharField(max_length=150)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Other')
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
