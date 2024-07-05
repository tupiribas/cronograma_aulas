from django.shortcuts import get_object_or_404, render
from .models import Mensagem


def hello_world(request, uuid):
    mensagem = get_object_or_404(Mensagem, id=uuid)
    return render(request, 'principal/hello_world.html', {'mensagem': mensagem})