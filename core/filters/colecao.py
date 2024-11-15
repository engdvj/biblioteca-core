from django_filters import rest_framework as filters
from core.models import Colecao

class ColecaoFiltro(filters.FilterSet):
    nome = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Colecao
        fields = ['nome']
