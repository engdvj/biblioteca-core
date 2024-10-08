from django_filters import rest_framework as filters
from core.models import Autor

class AutorFiltro(filters.FilterSet):
    nome = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Autor
        fields = ['nome']
