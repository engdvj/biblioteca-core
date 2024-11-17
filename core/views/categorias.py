from rest_framework import generics
from core.models.categoria import Categoria
from core.serializers.categoria import CategoriaSerializer, CategoriaLinkSerializer
from core.filters.categoria import CategoriaFiltro

# View para listar e criar categorias, usando o serializer que mostra apenas links
class CategoriaLista(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaLinkSerializer  # Usando o serializer que mostra apenas links
    filterset_class = CategoriaFiltro
    search_fields = ('^nome',)
    ordering_fields = ('nome',)
    name = 'Categorias cadastradas'

# View para detalhes de uma categoria específica
class CategoriaDetalhe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer  # Usando o serializer completo para detalhes
    name = 'Informações da categoria'
