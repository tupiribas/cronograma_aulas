from django.urls import path, include

urlpatterns = []


def registrar_urls(caminhos_lista: list):
    global urlpatterns
    urlpatterns += caminhos_lista

from .homepage_url import homepage_patterns
from .helloworld_url import helloworld_patterns
from .home_url import home_patterns
from .login_url import login_patterns
from .logout_url import logout_patterns