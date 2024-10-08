from django_filters import rest_framework as filters
from core.models import Categoria

class CategoriaFiltro(filters.FilterSet):
    nome = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Categoria
        fields = ['nome']
