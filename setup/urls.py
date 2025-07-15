from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('logiN.urls')), #redirecionamento de rota para o APP
]
