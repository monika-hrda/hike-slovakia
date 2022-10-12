from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """ Creates a form for the UserProfile model """
    class Meta:
        model = UserProfile
        fields = ('phone_number',)

    def __init__(self, *args, **kwargs):
        """
        Initializes the user profile form - adds placeholders and classes,
        removes auto-generated labels
        """
        super().__init__(*args, **kwargs)

        self.fields['phone_number'].widget.attrs['placeholder'] = 'Phone Number'
        self.fields['phone_number'].widget.attrs['class'] = 'border-black rounded-1 profile-form-input'
        self.fields['phone_number'].label = False


class UserForm(forms.ModelForm):
    """ Exposes some of the fields of user model for updating """
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)

    def __init__(self, *args, **kwargs):
        """
        Initialises the user form  - adds placeholders and classes, removes
        auto-generated labels and sets autofocus on first field
        """
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True

        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-1 profile-form-input'
            self.fields[field].label = False
