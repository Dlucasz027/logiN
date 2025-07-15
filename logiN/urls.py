from django.urls import path
from logiN.views import index

urlpatterns = [
    path('', index, name='index'),  # 👈 aqui define que a raiz ('') será atendida pela view index
]