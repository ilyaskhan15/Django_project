from django.urls import path
from .views import members

urlpatterns = [
    path('members/', members, name='members')
]