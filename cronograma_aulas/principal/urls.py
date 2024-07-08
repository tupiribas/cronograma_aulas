from django.urls import path

from .views import hello_world



urlpatterns = [
    path('hello/<uuid:uuid>/', hello_world, name='hello_world'),
]
