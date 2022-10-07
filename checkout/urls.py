from django.urls import path
from . import views

urlpatterns = [
    path('basket/<hike_id>/', views.view_basket, name='view_basket'),
    path('', views.checkout, name='checkout'),
    path('checkout_success/<booking_id>', views.checkout_success, name='checkout_success'),
]
