# Import necessary modules from Django
from django.db import models
# Import the custom user model
from django.contrib.auth import get_user_model

# Get the User model (instead of using 'User' directly, to support custom user models)
User = get_user_model()

# Category model represents product categories, such as "Landscape", "Nature", etc.
class Category(models.Model):
    """
    A model to represent product categories (e.g., Prints, Canvas, Photography).
    Categories help organize products in a logical structure.
    """
    class Meta:
        # Custom plural name for the Category model in admin
        verbose_name_plural = "Categories"

    # The name of the category (e.g., "Nature", "Abstract Art")
    name = models.CharField(max_length=254)
    
    # A more user-friendly version of the category name (optional)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        # When a category is represented as a string, return the name.
        return self.name

    def get_friendly_name(self):
        """
        Returns the friendly name for the category. If not provided, returns the name.
        """
        return self.friendly_name


# Print model represents the actual products that are being sold.
class Print(models.Model):
    """
    A model to represent a product (a 'Print'), with attributes like price,
    description, and images.
    """
    # Choices for the orientation of the print (Landscape, Portrait, Square)
    ORIENTATION_CHOICES = [
        ('L', 'Landscape'),
        ('P', 'Portrait'),
        ('S', 'Square'),
    ]

    # Foreign key linking the print to a specific category
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    
    # Stock Keeping Unit (SKU), optional, unique identifier for the product
    sku = models.CharField(max_length=254, null=True, blank=True)
    
    # Name of the print/product (e.g., "Golden Sunset")
    name = models.CharField(max_length=254)
    
    # Description of the print/product (e.g., "A beautiful golden sunset over the mountains.")
    description = models.TextField()
    
    # Price of the print/product (e.g., 19.99)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    # Orientation of the print (e.g., Landscape, Portrait, or Square)
    orientation = models.CharField(max_length=1, choices=ORIENTATION_CHOICES, default='S')
    
    # Rating of the print/product (optional)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    
    # Path to image 1 (as a string for storage location)
    image_1_path = models.CharField(max_length=1024, default='No Image')
    
    # Image field for image 1 (actual image file for display)
    image_1 = models.ImageField(default='No Image')
    
    # Path to image 2 (as a string for storage location)
    image_2_path = models.CharField(max_length=1024, default='No Image')
    
    # Image field for image 2 (actual image file for display)
    image_2 = models.ImageField(default='No Image')

    def __str__(self):
        # When a print product is represented as a string, return its name
        return self.name


# Review model represents customer reviews for the Print products.
class Review(models.Model):
    """
    A model for customer reviews on products (Prints). Each review is associated
    with a specific print and a specific user.
    """
    # Foreign key linking the review to a specific print product
    product = models.ForeignKey(Print, on_delete=models.CASCADE, related_name='reviews')
    
    # Foreign key linking the review to a specific user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    
    # The content of the review (feedback, comments)
    content = models.TextField()
    
    # Rating given to the product (e.g., 1-5 stars, or 1-10 scale)
    rating = models.IntegerField(default=5)
    # Default rating is set to 5 stars (out of 5)
    
    # Timestamp for when the review was created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Represent the review by the user's username who posted it
        return f"By {self.user.username}"
