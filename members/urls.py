from django.urls import path
from .views import members, details, main

urlpatterns = [
    path('', main, name='main'),
    path('members/', members, name='members'),
    path('members/details/<int:id>', details, name='detail' )
]