from django.urls import path
from . import views

urlpatterns = [
    path('basket/<hike_id>/', views.view_basket, name='view_basket'),
    path('', views.checkout, name='checkout'),
]
