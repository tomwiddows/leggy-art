from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


# Signal handler for when an OrderLineItem is saved (created or updated)
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update the order total when a line item is updated or created.
    This is triggered every time an OrderLineItem is saved.
    """
    instance.order.update_total()


# Signal handler for when an OrderLineItem is deleted
@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update the order total when a line item is deleted.
    This is triggered every time an OrderLineItem is deleted.
    """
    instance.order.update_total()
