from django.urls import path
from django.contrib import admin

from .views.helloworld_view import hello_world


urlpatterns = [
    path(route='admin/', view=admin.site.urls),
    path(route='hello/<uuid:uuid>/', view=hello_world, name='hello_world'),
    # path('', home, name='home'),
]
