from django.contrib import admin
from .models import Print, Category, Review

# Register your models here.
class PrintAdmin(admin.ModelAdmin):
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

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'content',
        'rating',
        'created_at',
    )


admin.site.register(Print, PrintAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)