from django.urls import path

from .view import hello_world


urlpatterns = [
    path('hello/<uuid:uuid>/', hello_world, name='hello_world'),
]
