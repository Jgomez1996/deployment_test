from django.urls import path
from . import views

urlpatterns = [
    path('shows', views.index),
    path('shows/new', views.create_show),
    path('shows/create', views.create_form),
    path('shows/<int:show_id>', views.show_show),
    path('shows/<int:show_id>/destroy', views.delete_show),
    path('shows/<int:show_id>/edit', views.edit_show),
    path('shows/<int:show_id>/update', views.update_show),
]
