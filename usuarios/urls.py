from django.urls import path #Módulo para definir URLs/ path é a função que conecta uma URL | Importing path function
from usuarios.views import login, cadastro, logout #Import das Views que serão usadas nas URLs | Importing views for the URLs

urlpatterns = [ #Lista especial do Django, URLS disponíveis do projeto | List of available URLs in the project
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'), #'Cadastro' é a URL, Cadastro é a view, nmae='Cadastro' é o nome que vai ser usado internamente
    path('logout', logout, name='logout'),
]