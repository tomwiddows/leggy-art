# Import necessary Django modules
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Import the CountryField from the django_countries package
from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A user profile model for maintaining default delivery information
    and order history for a user.
    """

    # Link the user profile to the built-in Django User model with a OneToOneField.
    # This means each User can have only one UserProfile associated with it.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # The following fields store the user's default delivery information.
    # All fields are optional, as indicated by null=True, blank=True
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)  # User's default phone number
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)  # Primary street address
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)  # Secondary street address (if any)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)  # User's town or city
    default_county = models.CharField(max_length=80, null=True, blank=True)  # User's county (if applicable)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)  # User's postal code
    default_country = CountryField(blank_label='Country', null=True, blank=True)  # Country of residence (using a third-party CountryField)

    def __str__(self):
        # Returns the username of the associated User object when the profile is displayed.
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Signal to create or update a UserProfile when a User instance is created or saved.
    This ensures that a profile is always created for a user upon registration
    and is kept updated when the user object is saved.
    """
    
    if created:
        # If the user is newly created, create a corresponding UserProfile for them.
        UserProfile.objects.create(user=instance)
    
    # For existing users, just save their profile (to update any changes).
    instance.userprofile.save()
