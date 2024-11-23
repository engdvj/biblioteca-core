from rest_framework import generics
from core.models.categoria import Categoria
from core.serializers.categoria import CategoriaSerializer
from core.serializers.relacionados import CategoriaLinkSerializer
from core.filters.categoria import CategoriaFiltro

class CategoriaLista(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaLinkSerializer 
    filterset_class = CategoriaFiltro
    search_fields = ('^nome',)
    ordering_fields = ('nome',)
    name = 'Categorias cadastradas'


class CategoriaDetalhe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer  
    name = 'Informações da categoria'
