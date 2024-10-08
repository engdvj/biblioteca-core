from django_filters import rest_framework as filters
from .models import Livro, Autor, Categoria

class LivroFiltro(filters.FilterSet):
    nome = filters.CharFilter(lookup_expr='icontains')
    autor = filters.CharFilter(field_name='autor__nome', lookup_expr='icontains')  # name -> nome, author -> autor
    categoria = filters.AllValuesFilter(field_name='categoria__nome')  # category -> categoria

    class Meta:
        model = Livro  # Atualizado
        fields = ['nome', 'autor', 'categoria', 'publicado']  # name -> nome, etc.

class AutorFiltro(filters.FilterSet):
    nome = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Autor  # Atualizado
        fields = ['nome']  # name -> nome

class CategoriaFiltro(filters.FilterSet):
    nome = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Categoria  # Atualizado
        fields = ['nome']  # name -> nome

