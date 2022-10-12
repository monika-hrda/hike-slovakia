from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """ Creates a form for the UserProfile model """
    class Meta:
        model = UserProfile
        fields = ('phone_number',)

    def __init__(self, *args, **kwargs):
        """
        Initializes the user profile form - adds placeholders and classes,
        removes auto-generated labels and sets autofocus on first field
        """
        super().__init__(*args, **kwargs)

        # self.fields['phone_number'].widget.attrs['autofocus'] = True
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Phone Number'
        self.fields['phone_number'].widget.attrs['class'] = 'border-black rounded-1 profile-form-input'
        self.fields['phone_number'].label = False
