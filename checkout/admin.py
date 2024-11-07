# Import necessary modules from Django
from django.contrib import admin  # Django's admin interface
from .models import Order, OrderLineItem  # The Order and OrderLineItem models to be registered with the admin interface

# Inline admin class for displaying OrderLineItem details within the Order admin page
class OrderLineItemAdminInline(admin.TabularInline):
    """
    An inline admin class to display OrderLineItem instances 
    as part of the Order detail page in the admin panel.
    """
    model = OrderLineItem  # Model to be displayed in the inline section
    readonly_fields = ('lineitem_total',)  # The fields to be shown as read-only, like the total cost for each line item


# Admin class for customizing the display of Order objects in the admin interface
class OrderAdmin(admin.ModelAdmin):
    """
    Custom admin interface for the Order model.
    Adds inlines for OrderLineItems and specifies which fields to display and how.
    """
    inlines = (OrderLineItemAdminInline,)  # Include the OrderLineItemAdminInline to show line items within the Order page

    # Define fields that should be read-only in the admin panel
    readonly_fields = ('order_number', 'date',  # Display these fields as read-only (they can't be edited in the admin)
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_basket',
                       'stripe_pid')

    # Define the fields to be shown in the Order form in the admin panel
    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_basket',
              'stripe_pid')

    # Fields to be displayed in the list view of the Order model in the admin panel
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total')

    # Define the ordering of the orders in the list view (by date, in descending order)
    ordering = ('-date',)  # Orders will be shown with the most recent first


# Register the Order model with the custom OrderAdmin class
admin.site.register(Order, OrderAdmin)  # This will make the Order model appear in the admin interface with the defined settings
