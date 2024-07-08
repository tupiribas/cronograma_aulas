from django.urls import path, include

urlpatterns = []

def registrar_urls(caminhos_lista: list):
    global urlpatterns
    urlpatterns += caminhos_lista

from .home_url import home_patterns
from .helloworld_url import helloworld_patterns
