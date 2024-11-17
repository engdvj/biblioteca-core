from rest_framework import generics
from core.models.autor import Autor
from core.serializers.autor import AutorSerializer, AutorLinkSerializer
from core.filters.autor import AutorFiltro

# View para listar e criar autores, usando o serializer que mostra apenas links
class AutorLista(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorLinkSerializer  # Usando o serializer que mostra apenas links
    filterset_class = AutorFiltro
    search_fields = ('^nome',)
    ordering_fields = ('nome',)
    name = 'Autores cadastrados'

# View para detalhes de um autor específico
class AutorDetalhe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer  # Usando o serializer completo para detalhes
    name = 'Informações do autor'
