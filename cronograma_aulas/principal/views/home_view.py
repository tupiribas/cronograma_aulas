from . import render_view


def home(request):
    return render_view(request, 'principal/home.html')
