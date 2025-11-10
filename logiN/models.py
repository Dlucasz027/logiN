from django.db import models #Módulo que cira tabelas no banco de dados | Module that creates tables in the database
from datetime import datetime #Import para manipulação de data e hora | Import for date and time manipulation
from django.contrib.auth.models import User #Modelo padrão de usuários para relacionar as imagens upadas ao próprio user | Default user model to relate uploaded images to the user

class Upload(models.Model):

    OPCOES_CATEGORIA = [
        ("UPLOAD","Upload"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicacao = models.BooleanField(default=False)
    data = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user'
    )

    def __str__(self):
        return self.nome
