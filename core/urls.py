from core.views.livros import LivroLista, LivroDetalhe
from core.views.autores import AutorLista, AutorDetalhe
from core.views.categorias import CategoriaLista, CategoriaDetalhe
from core.views.api_raiz import ApiRaiz
from django.urls import path


urlpatterns = [
    path('', ApiRaiz.as_view(), name='api-root'),
    path('livros/', LivroLista.as_view(), name='lista-livros'),
    path('livros/<int:pk>/', LivroDetalhe.as_view(), name='detalhe-livro'),
    path('autores/', AutorLista.as_view(), name='lista-autores'),
    path('autores/<int:pk>/', AutorDetalhe.as_view(), name='detalhe-autor'),
    path('categorias/', CategoriaLista.as_view(), name='lista-categorias'),
    path('categorias/<int:pk>/', CategoriaDetalhe.as_view(), name='detalhe-categoria'),
]
