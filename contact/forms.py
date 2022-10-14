from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Form for Contact model """
    class Meta:
        model = Contact
        fields = ['contact_email', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        """
        Initialises the user form  - adds placeholders and classes, removes
        auto-generated labels and sets autofocus on first field
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            'contact_email': 'Email Address',
            'subject': 'Subject',
            'message': 'Your message',
        }

        self.fields['contact_email'].widget.attrs['autofocus'] = True

        for field in self.fields:
            self.fields[field].widget.attrs[
                'placeholder'] = f'{placeholders[field]} *'
            self.fields[field].widget.attrs['class'] = 'border-black '
            'rounded-1 contact-form-input'
            self.fields[field].label = False
