from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from products.models import Print
from profiles.models import UserProfile

import json
import time
import stripe


class StripeWH_Handler:
    """Handle Stripe webhooks."""

    def __init__(self, request):
        """
        Initialize the webhook handler with the request object.

        Args:
            request: The incoming HTTP request.
        """
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email."""

        # Get the customer's email from the order
        cust_email = order.email

        # Prepare the subject and body of the confirmation email using templates
        subject = render_to_string(
            'checkout/confirmation_email/confirmation_email_subject.txt',
            {'order': order}
        )
        body = render_to_string(
            'checkout/confirmation_email/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
        )
        
        # Send the email to the customer
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """Handle a generic/unknown/unexpected webhook event."""

        # Return an HTTP response indicating that the event was not handled
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """Handle the payment_intent.succeeded webhook from Stripe."""

        # Extract necessary data from the event
        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info

        # Retrieve the charge details from Stripe
        stripe_charge = stripe.Charge.retrieve(intent.latest_charge)

        # Get billing and shipping details from the charge object
        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        # Clean empty fields in the shipping address
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if the user opted to save it
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            # Retrieve the user's profile if they are logged in
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                # Update the profile with shipping details
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address1 = shipping_details.address.line1
                profile.default_street_address2 = shipping_details.address.line2
                profile.default_county = shipping_details.address.state
                profile.save()

        order_exists = False
        attempt = 1

        # Retry up to 5 times to find an existing order matching the payment details
        while attempt <= 5:
            try:
                # Attempt to find the order that matches the payment details
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                # Retry if order is not found and increment the attempt counter
                attempt += 1
                time.sleep(1)
        
        if order_exists:
            # Send confirmation email if the order is already found
            self._send_confirmation_email(order)

            # Return a success response indicating the order was verified
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified '
                        'order already in database',
                status=200
            )
        else:
            order = None
            try:
                # Create a new order if one does not exist in the database
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_basket=basket,
                    stripe_pid=pid,
                )

                # Loop through the basket and create order line items for each product
                for item_id, item_data in json.loads(basket).items():
                    product = Print.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for quantity in item_data.items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                            )
                            order_line_item.save()
            except Exception as e:
                # Delete the order if an error occurs during creation
                if order:
                    order.delete()

                # Return an error response if the order creation fails
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500
                )

        # Send the confirmation email once the order has been created
        self._send_confirmation_email(order)

        # Return a success response for the successfully handled webhook
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """Handle the payment_intent.payment_failed webhook from Stripe."""

        # Return a generic success response for failed payments
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
