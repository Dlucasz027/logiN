from django.apps import AppConfig #Modulo de gerenciamento dos app Django | Module for managing Django apps
class UsuariosConfig(AppConfig): #App config herda as configurações importadas do django.apps | App config inherits configurations from django.apps
    default_auto_field = 'django.db.models.BigAutoField' #Atributo default_auto_field para definir o campo automático da primary key | default_auto_field attribute to define the automatic primary key field
    name = 'usuarios' #Nome do app | Name of the app
