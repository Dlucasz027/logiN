from django.urls import path
from logiN.views import index, exclusiva

urlpatterns = [
    path('', index, name='index'),  # 👈 aqui define que a raiz ('') será atendida pela view index
    path('exclusiva/', exclusiva, name='exclusiva'), #area depois de fazer login, exclusiva
]