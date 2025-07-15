from django.shortcuts import render

def index(request):
    return render(request, "logiN/index.html")  #caminho para o HTML

