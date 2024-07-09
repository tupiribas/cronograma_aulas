import uuid

from .home_view import home

from . import login_required, redirect


@login_required
def redireciona_apos_login(request):
    # Gerar UUID para a seção
    id_sessao = uuid.uuid4()
    # Redirecionar para a URL com o UUID
    return redirect(home, id_sessao=id_sessao)
