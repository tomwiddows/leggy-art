# Import necessary modules from Django
from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    """
    A form for updating the user profile, allowing users to edit their personal
    details such as address, phone number, and other profile-related fields.
    """
    
    # Meta class defines model and fields for the form
    class Meta:
        model = UserProfile  # The form will interact with the UserProfile model
        exclude = ('user',)  # Exclude the 'user' field from the form (this is handled automatically)

    def __init__(self, *args, **kwargs):
        """
        Custom initialization for the form to:
        - Add placeholders to fields for better user guidance
        - Add CSS classes to fields for styling
        - Remove auto-generated labels to use custom placeholders and improve form appearance
        - Set autofocus on the first field for a better user experience
        """
        super().__init__(*args, **kwargs)  # Call the parent class constructor to initialize the form

        # A dictionary to map fields to their corresponding placeholders
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        # Set autofocus on the phone number field (the first field in the form)
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True

        # Iterate over each field in the form and customize it
        for field in self.fields:
            if field != 'default_country':  # Skip 'default_country' because it may be a dropdown field
                # Add a placeholder and append a '*' if the field is required
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]

                # Set the placeholder for the field
                self.fields[field].widget.attrs['placeholder'] = placeholder

            # Add CSS classes to each field for styling (e.g., to make input fields uniform)
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'

            # Remove the default label for each field, so that placeholders are used instead
            self.fields[field].label = False
