from django.shortcuts import render, redirect
from django.contrib import messages

def exclusiva(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado.')
        return redirect('login')

    return render(request, "logiN/exclusiva.html")