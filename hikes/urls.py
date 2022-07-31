from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_hikes, name='hikes'),
    path('<hike_id>', views.hike_detail, name='hike_detail'),
]
