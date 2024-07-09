from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from ..models import Mensagem

render = render
get_object_or_404 = get_object_or_404
Mensagem = Mensagem
login_required = login_required
redirect = redirect
