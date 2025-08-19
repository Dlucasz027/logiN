from django.db import models #Módulo que cira tabelas no banco de dados | Module that creates tables in the database
from datetime import datetime #Import para manipulação de data e hora | Import for date and time manipulation
from django.contrib.auth.models import User #Modelo padrão de usuários para relacionar as imagens upadas ao próprio user | Default user model to relate uploaded images to the user

class Fotografia(models.Model): #Classe com models.model vira tabela no banco de dados | Class with models.Model creates a table in the database

    OPCOES_CATEGORIA = [
        ("FOTOGRAFIA","Fotografia"), #Categoria das imagens inseridas | Category of the inserted images
    ]

#Campos da tabela | Fields of the table
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user'
    )

    def __str__(self): #Método especial para retornar o nome da imagem conforme definido no campo nome | Special method to return the name of the image as defined in the name field
        return self.nome
