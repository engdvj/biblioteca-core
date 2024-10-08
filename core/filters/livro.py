from django_filters import rest_framework as filters
from core.models import Livro

class LivroFiltro(filters.FilterSet):
    nome = filters.CharFilter(lookup_expr='icontains')
    autor = filters.CharFilter(field_name='autor__nome', lookup_expr='icontains')
    categoria = filters.AllValuesFilter(field_name='categoria__nome')

    class Meta:
        model = Livro
        fields = ['nome', 'autor', 'categoria', 'publicado']
