from . import get_object_or_404, render_view, Mensagem


def hello_world(request, uuid):
    mensagem = get_object_or_404(Mensagem, id=uuid)
    return render_view(request, 'principal/hello_world.html', {'mensagem': mensagem})
