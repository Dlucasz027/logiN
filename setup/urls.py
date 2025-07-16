from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('logiN.urls')),
    path('', include('usuarios.urls')), #redirecionamento de rota para o APP
]
