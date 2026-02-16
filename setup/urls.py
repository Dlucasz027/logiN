from django.contrib import admin #Ativa o painel de administração | Activates the admin panel
from django.urls import path, include #path para mapear rotas, include para delegar rotas a outros arquivos | path to map routes, include to delegate routes to other files
from django.conf import settings #Importa as configurações do projeto | Imports the project settings
from django.conf.urls.static import static #Importa as configurações de arquivos estáticos | Imports static file settings

urlpatterns = [ #Lista especial de URLs | Special list of URLs
    path('admin/', admin.site.urls), #Rota padrão do painel de administração | Default route for the admin panel
    path('', include('logiN.urls')), #Apontamento com include para os respectivos APPS | Pointing with include to the respective APPS
    path('', include('usuarios.urls')), #redirecionamento de rota para o APP
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #Suporte para envio de arquivos de mídia pelo usuário | Support for user-uploaded media files
