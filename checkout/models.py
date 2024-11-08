import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Print
from profiles.models import UserProfile


class Order(models.Model):
    # Unique order identifier, automatically generated
    order_number = models.CharField(
        max_length=32, null=False, editable=False
    )
    
    # Relationship to the UserProfile model (optional foreign key)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='orders'
    )
    
    # Customer's full name for the order
    full_name = models.CharField(max_length=50, null=False, blank=False)
    
    # Customer's email address
    email = models.EmailField(max_length=254, null=False, blank=False)
    
    # Customer's phone number
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    
    # Country selected by the customer using a dropdown
    country = CountryField(
        blank_label='Country *', null=False, blank=False
    )
    
    # Postcode for the delivery address (optional)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    
    # Town or city for the delivery address
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    
    # First line of the street address
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    
    # Second line of the street address (optional)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    
    # County or region (optional)
    county = models.CharField(max_length=80, null=True, blank=True)
    
    # Date and time the order was placed
    date = models.DateTimeField(auto_now_add=True)
    
    # Delivery cost (calculated based on the order)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
    )
    
    # Total cost of the items in the order
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    
    # Grand total, including delivery cost
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    
    # A string representation of the customer's basket before checkout
    original_basket = models.TextField(null=False, blank=False, default='')
    
    # Stripe Payment Intent ID for the order
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default=''
    )

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID.
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update the grand total each time a line item is added, accounting 
        for delivery costs.
        """
        # Aggregate the total price of the order's line items
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total')
        )['lineitem_total__sum'] or 0
        
        # Calculate delivery cost if order total is below the free delivery threshold
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = settings.BASELINE_DELIVERY_FEE + (
                self.order_total * settings.EXTRA_DELIVERY_PERCENTAGE
            ) / 100
        else:
            self.delivery_cost = 0
        
        # Calculate the grand total (order total + delivery cost)
        self.grand_total = self.order_total + self.delivery_cost
        
        # Save the updated order object
        self.save()


    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order, null=False, blank=False, on_delete=models.CASCADE,
        related_name='lineitems'
    )
    product = models.ForeignKey(
        Print, null=False, blank=False, on_delete=models.CASCADE
    )
    quantity = models.IntegerField(
        null=False, blank=False, default=0
    )
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False
    )


    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
        