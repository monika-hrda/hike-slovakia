from django.urls import path
from . import views

urlpatterns = [
    path('<hike_id>', views.checkout, name='checkout')
]