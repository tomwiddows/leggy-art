from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Print(models.Model):
    ORIENTATION_CHOICES = [
        ('L', 'Landscape'),
        ('P', 'Portrait'),
        ('S', 'Square'),
    ]

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    orientation = models.CharField(max_length=1, choices=ORIENTATION_CHOICES, default='S')
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_1_path = models.CharField(max_length=1024, default='No Image')
    image_1 = models.ImageField(default='No Image')
    image_2_path = models.CharField(max_length=1024, default='No Image')
    image_2 = models.ImageField(default='No Image')

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Print, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField()
    rating = models.IntegerField(default=5)  # Assuming a rating system
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"By {self.user.username}"