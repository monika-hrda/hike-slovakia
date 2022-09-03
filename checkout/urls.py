from django.urls import path
from . import views

urlpatterns = [
    path('<hike_id>', views.view_checkout, name='view_checkout')
]
