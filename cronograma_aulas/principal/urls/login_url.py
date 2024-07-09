from . import registrar_urls
from django.urls import path
from django.contrib.auth import views as auth_view

login_patterns = [
    path(route='login/',
         view=auth_view.LoginView.as_view(template_name='principal/login.html'), name='login')
]

# Registrar URLs
registrar_urls(login_patterns)
