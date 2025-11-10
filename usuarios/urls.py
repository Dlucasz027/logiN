from django.urls import path
from usuarios.views import login, cadastro, logout

urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'),
    path('logout/', logout, name='logout')
]