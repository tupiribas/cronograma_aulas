from django.urls import path

from . import registrar_urls
from ..views.helloworld_view import hello_world

helloworld_patterns = [
    path(route='hello/<uuid:uuid>/', view=hello_world, name='hello')
]

# Registrar URLs
registrar_urls(helloworld_patterns)
