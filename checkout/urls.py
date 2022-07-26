from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('basket/<hike_id>/', views.view_basket, name='view_basket'),
    path('', views.checkout, name='checkout'),
    path('checkout_success/<booking_number>',
         views.checkout_success,
         name='checkout_success'),
    path('wh/', webhook, name='webhook'),
]
