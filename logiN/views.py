from django.shortcuts import render, get_object_or_404, redirect # Importa funções para renderizar templates e redirecionar | Import functions to render templates and redirect
from django.contrib import messages # Importa mensagens para feedback ao usuário | Import messages for user feedback
from logiN.models import Fotografia # Importa o model Fotografia | Import the Fotografia model

def index(request):
    return render(request, "logiN/index.html")  # Retorna e renderiza o template index.html | Returns and renders the index.html template

def exclusiva(request):
    if not request.user.is_authenticated: # Verifica se o usuário está autenticado | Check if the user is authenticated
        messages.error(request, 'Você precisa estar logado.')
        return redirect('login')

    return render(request, "logiN/exclusiva.html") # Retorna e renderiza o template exclusiva.html, se o usuário estiver autenticado | Returns and renders the exclusiva.html template, if the user is authenticated