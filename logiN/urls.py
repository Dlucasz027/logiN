from django.urls import path # Importa o módulo path responsável por definir URLs | Import the path module responsible for defining URLs
from logiN.views import index, exclusiva  # Importa as views index e exclusiva do módulo views | Import the index and exclusiva views from the views module

urlpatterns = [  # Lista especial do Django que contém as URLs do aplicativo | Special Django list that contains the app's URLs
    path('', index, name='index'),  
    path('exclusiva/', exclusiva, name='exclusiva'), # exclusiva/ representa a URL para acessar a página, exclusiva é importada das views e por último o nome que será usado para referenciar essa URL | 'exclusiva/' represents the URL to access the page, exclusiva is imported from views, and finally the name that will be used to reference this URL
]