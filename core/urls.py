from core.views.livros import LivroLista, LivroDetalhe
from core.views.autores import AutorLista, AutorDetalhe
from core.views.categorias import CategoriaLista, CategoriaDetalhe
from core.views.api_raiz import ApiRaiz
from django.urls import path


urlpatterns = [
    path('', ApiRaiz.as_view(), name='api-root'),
    path('livros/', LivroLista.as_view(), name='Livros cadastrados'),
    path('livros/<int:pk>/', LivroDetalhe.as_view(), name='Informações do livro'),
    path('autores/', AutorLista.as_view(), name='Autores cadastrados'),
    path('autores/<int:pk>/', AutorDetalhe.as_view(), name='Informações do autor'),
    path('categorias/', CategoriaLista.as_view(), name='Categorias cadastradas'),
    path('categorias/<int:pk>/', CategoriaDetalhe.as_view(), name='Informações da categoria'),
]
