from rest_framework import generics
from core.models.autor import Autor
from core.serializers.autor import AutorSerializer
from core.filters.autor import AutorFiltro


class AutorLista(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    filterset_class = AutorFiltro
    search_fields = ('^nome',)
    ordering_fields = ('nome',)
    name = 'lista-autores'

class AutorDetalhe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = 'detalhe-autor'
