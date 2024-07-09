from .import registrar_urls
from django.urls import path
from ..views.home_view import home

home_patterns = [
    path(route='home/<uuid:id_sessao>/', view=home, name='home')
]

# Registrar URLs
registrar_urls(home_patterns)
