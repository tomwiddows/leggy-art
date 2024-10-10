from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    try:
        def ready(self):
            import checkout.signals
    except Exception as e:
        messages.error(error, 'e')
