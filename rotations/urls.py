# rotations/urls.py
from django.urls import path
from . import views

app_name = 'rotations'
urlpatterns = [
    path('',    views.rotation_list, name='list'),
    path('add/',views.add_rotation, name='add'),
]