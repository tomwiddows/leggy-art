from django import forms
from .widgets import CustomClearableFileInput
from .models import Print, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Print
        fields = '__all__'

    image_1 = forms.ImageField(label='Image 1', required=False, widget=CustomClearableFileInput)
    image_2 = forms.ImageField(label='Image 2', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories] #list comporehension

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
