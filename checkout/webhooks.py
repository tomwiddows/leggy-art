from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWH_Handler

import stripe

@require_POST
@csrf_exempt
def webhook(request):
    """Listen for webhooks from Stripe."""

    # Setup: Get the Stripe secret key and set the API key
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get the payload and signature header from the request
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        # Verify the webhook signature and construct the event object
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        # If payload is invalid, return a 400 Bad Request response
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # If signature verification fails, return a 400 Bad Request response
        return HttpResponse(status=400)
    except Exception as e:
        # Return a 400 Bad Request response for any other errors
        return HttpResponse(content=e, status=400)

    # Initialize the webhook handler with the request
    handler = StripeWH_Handler(request)

    # Map Stripe event types to handler functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }

    # Get the type of event from Stripe
    event_type = event['type']

    # Get the corresponding handler for the event type, default to a generic handler
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the appropriate handler function for the event and return its response
    response = event_handler(event)
    return response
