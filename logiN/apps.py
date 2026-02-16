from django.apps import AppConfig  #Importa AppConfig do módulo django.apps | Import AppConfig from the django.apps module

class LoginConfig(AppConfig):  #Cria a classe LoginConfig que herda de AppConfig | Create the LoginConfig class that inherits from AppConfig
    default_auto_field = 'django.db.models.BigAutoField'  # Atributo especial com campo padrão para chaves primárias | Special attribute with default field for primary keys
    name = 'logiN'
