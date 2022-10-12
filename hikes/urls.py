from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_hikes, name='hikes'),
    path('<hike_id>', views.hike_detail, name='hike_detail'),
    path('add_hike/', views.add_hike, name='add_hike'),
    path('edit_hike/<hike_id>/', views.edit_hike, name='edit_hike'),
    path('delete_hike/<hike_id>/', views.delete_hike, name='delete_hike'),
]
