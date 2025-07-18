from django.shortcuts import render
from usuarios.forms import LoginForms

def login(request):
    form = LoginForms()  #função login
    return render(request, "logiN/login.html", {"form": form})

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')