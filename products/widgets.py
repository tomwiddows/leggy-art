# Import relevant django packages
from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """
    Custom widget for file input fields, extending Django's built-in ClearableFileInput.
    This widget allows the user to clear or remove the file uploaded and provides 
    a more customized appearance and functionality for handling file uploads.
    """
    
    # Label for the checkbox that will allow the user to remove the uploaded file.
    clear_checkbox_label = _('Remove')
    
    # Text shown next to the uploaded file to indicate that it is the current file.
    initial_text = _('Current Image')
    
    # Text shown on the file input button when no file is selected (empty string in this case).
    input_text = _('')  # Empty text to avoid showing anything beside the file input.

    # Path to the custom HTML template that will render this widget.
    # This template is used to customize the rendering of the clearable file input field.
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'
