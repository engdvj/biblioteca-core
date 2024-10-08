from rest_framework import generics
from core.models.categoria import Categoria
from core.serializers.categoria import CategoriaSerializer
from core.filters.categoria import CategoriaFiltro


class CategoriaLista(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filterset_class = CategoriaFiltro
    search_fields = ('^nome',)
    ordering_fields = ('nome',)
    name = 'Categorias cadastradas'

class CategoriaDetalhe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = 'Informações da categoria'
