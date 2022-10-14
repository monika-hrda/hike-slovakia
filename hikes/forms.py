from django import forms
from .models import Hike


class HikeForm (forms.ModelForm):
    """ Form to create and edit hikes """
    class Meta:
        model = Hike
        fields = ['difficulty', 'title', 'description', 'price', 'image']

        labels = {
            'title': 'Hike Name',
            'difficulty': 'Difficulty',
            'description': 'Description',
            'price': 'Price',
            'image': 'Image  (use image in landscape orientation - 1920x1280)',
        }
