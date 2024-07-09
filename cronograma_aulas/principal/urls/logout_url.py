from . import registrar_urls
from django.urls import path
from django.contrib.auth import views as auth_view

logout_patterns = [
    path(route='logout/',
         view=auth_view.LogoutView.as_view(), name='logout')
]

# Registrar URLs
registrar_urls(logout_patterns)
