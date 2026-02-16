from django.urls import path
from logiN.views import exclusiva
from usuarios.views import login as usuarios_login

urlpatterns = [
    path('', usuarios_login, name='login'),
    path('exclusiva/', exclusiva, name='exclusiva')
]