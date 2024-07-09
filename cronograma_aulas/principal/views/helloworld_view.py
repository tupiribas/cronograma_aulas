from . import get_object_or_404, render, Mensagem


def hello_world(request, uuid):
    mensagem = get_object_or_404(Mensagem, id=uuid)
    return render(request, 'principal/hello_world.html', {'mensagem': mensagem})
