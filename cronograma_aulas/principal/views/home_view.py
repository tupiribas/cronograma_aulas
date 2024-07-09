from . import render, login_required


@login_required
def home(request, id_sessao):
    # Aqui você pode fazer o que for necessário com o UUID
    return render(request, 'home.html', {'id': id_sessao})
