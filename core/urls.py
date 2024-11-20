from django.urls import path
from core.views import ApiRaiz
from core.views.livros import LivroLista, LivroDetalhe
from core.views.autores import AutorLista, AutorDetalhe
from core.views.categorias import CategoriaLista, CategoriaDetalhe
from core.views.colecao import ColecaoLista, ColecaoDetalhe
from core.views.login import Login
from core.views.index import index
from core.views.debug import debug_auth
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    
    # Endpoints para login 
    path('', index, name='index'),  # Tela de login
    path('api/login/', Login.as_view(), name='login'),  # Login endpoint
    path('api/', ApiRaiz.as_view(), name='api-root'),  # Página inicial após login
    path('debug-auth/', debug_auth),
    
    # Endpoints do schema e da documentação
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),  # Endpoint do schema
    path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # Documentação com Swagger
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),  # Documentação com Redoc

    # Endpoints para a API
    ## URLs para livros
    path('livros/', LivroLista.as_view(), name='livros-lista'),
    path('livros/<int:pk>/', LivroDetalhe.as_view(), name='livro-detail'),  # Certifique-se de que o nome é 'livro-detail'

    ## URLs para autores
    path('autores/', AutorLista.as_view(), name='autores-lista'),
    path('autores/<int:pk>/', AutorDetalhe.as_view(), name='autor-detail'),  # Nome correto

    ## URLs para categorias
    path('categorias/', CategoriaLista.as_view(), name='categorias-lista'),
    path('categorias/<int:pk>/', CategoriaDetalhe.as_view(), name='categoria-detail'),  # Nome correto

    ## URLs para coleções
    path('colecoes/', ColecaoLista.as_view(), name='colecoes-lista'),
    path('colecoes/<int:pk>/', ColecaoDetalhe.as_view(), name='colecao-detail'),  # Nome correto
]
