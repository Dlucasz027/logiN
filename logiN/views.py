from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from logiN.models import Fotografia

def index(request):
    return render(request, "logiN/index.html")  #caminho para o HTML

def exclusiva(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado.')
        return redirect('login')

    return render(request, "logiN/exclusiva.html")