from django.urls import path
from .views import members, details

urlpatterns = [
    path('members/', members, name='members'),
    path('members/details/<int:id>', details, name='detail' )
]