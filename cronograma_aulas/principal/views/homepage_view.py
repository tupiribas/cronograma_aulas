from . import render


def homepage(request):
    return render(request, 'principal/homepage.html')
