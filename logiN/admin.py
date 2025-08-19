from django.contrib import admin #Módulo do painel administrativo do Django | Django admin panel module
from logiN.models import Fotografia #Importando o model de models.py | Importing the model from models.py

class ListandoFotografias(admin.ModelAdmin): #admin.ModelAdmin é uma classe que permite personalizar a exibição com listagens, filtro, edição e etc
    list_display = ("id", "nome", "legenda", "publicada")  #Campos que serão exibidos na listagem | Fields to display in the list view
    list_display_links = ("id","nome")  #Campos clicáveis (list_display_links) | Fields clickable in the list view
    search_fields = ("nome",)  #Campo de busca | Search field
    list_filter = ("categoria", 'usuario')  #Campos de filtro | Filter fields
    list_editable = ("publicada",)  #Campos editáveis diretamente na listagem | Fields editable directly in the list view
    list_per_page = 10  #Páginação de itens por página | Items per page

admin.site.register(Fotografia, ListandoFotografias)  #Registra o model no painel administrativo do Django | Register the model in the Django admin panel