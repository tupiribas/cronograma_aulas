from .import registrar_urls
from django.urls import path
from ..views.homepage_view import homepage

homepage_patterns = [
    path(route='', view=homepage, name='homepage')
]

# Registrar URLs
registrar_urls(homepage_patterns)
