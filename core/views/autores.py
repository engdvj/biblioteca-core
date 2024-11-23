from rest_framework import generics
from core.models.autor import Autor
from core.serializers.autor import AutorSerializer
from core.serializers.relacionados import AutorLinkSerializer
from core.filters.autor import AutorFiltro

class AutorLista(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    filterset_class = AutorFiltro
    search_fields = ('^nome',)
    ordering_fields = ('nome',)
    name = 'Autores cadastrados'

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AutorSerializer
        return AutorLinkSerializer

class AutorDetalhe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = 'Informações do autor'
