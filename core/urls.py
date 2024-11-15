from django.urls import path
from core.views import ApiRaiz
from core.views.livros import LivroLista, LivroDetalhe
from core.views.autores import AutorLista, AutorDetalhe
from core.views.categorias import CategoriaLista, CategoriaDetalhe
from core.views.colecao import ColecaoLista, ColecaoDetalhe
from core.views.login import Login
from core.views.api_raiz import ApiRaiz
from core.views.index import index


urlpatterns = [
    

    path('', index, name='index'),  # Tela de login (index.html)
    path('api/login/', Login.as_view(), name='login'),  # Endpoint de login
    path('api/', ApiRaiz.as_view(), name='api-root'),  # API_ROOT com as informações das coleções


    # Endpoints para a API
    path('livros/', LivroLista.as_view(), name='livros-lista'),
    path('livros/<int:pk>/', LivroDetalhe.as_view(), name='livro-detalhe'),
    path('autores/', AutorLista.as_view(), name='autores-lista'),
    path('autores/<int:pk>/', AutorDetalhe.as_view(), name='autor-detalhe'),
    path('categorias/', CategoriaLista.as_view(), name='categorias-lista'),
    path('categorias/<int:pk>/', CategoriaDetalhe.as_view(), name='categoria-detalhe'),
    path('colecoes/', ColecaoLista.as_view(), name='colecoes-lista'),
    path('colecoes/<int:pk>/', ColecaoDetalhe.as_view(), name='colecao-detalhe'),
]
