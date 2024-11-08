# Import the necessary modules from Django's admin interface
from django.contrib import admin
from .models import Print, Category, Review


# Admin configuration for the Print model
class PrintAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the 'Print' model. This class determines how
    the 'Print' model is displayed in the Django admin interface.
    """
    # The list of fields to display in the product list view in the admin
    # interface
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'orientation',
        'rating',
        'image_1_path',
        'image_1',
        'image_2_path',
        'image_2',
    )

    # Ordering the products by SKU by default in the admin list view
    ordering = ('sku',)


# Admin configuration for the Category model
class CategoryAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the 'Category' model. This class controls how
    categories are displayed in the admin interface.
    """
    # The fields to display for each category in the admin interface
    list_display = (
        'friendly_name',      # The user-friendly name of the category
        'name',               # The actual name of the category
    )


# Admin configuration for the Review model
class ReviewAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the 'Review' model. This class determines how
    the reviews are displayed in the admin interface.
    """
    # The fields to display for each review in the admin interface
    list_display = (
        'product',
        'user',
        'content',
        'rating',
        'created_at',
    )

# Registering the models with their respective custom admin classes
# This makes them available and editable in the Django admin interface

# Register the 'Print' model with the 'PrintAdmin' class
admin.site.register(Print, PrintAdmin)
# Register the 'Category' model with the 'CategoryAdmin' class
admin.site.register(Category, CategoryAdmin)
# Register the 'Review' model with the 'ReviewAdmin' class
admin.site.register(Review, ReviewAdmin)  
