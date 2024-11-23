from rest_framework import generics
from core.models.livro import Livro
from core.serializers.livro import LivroSerializer
from core.serializers.relacionados import LivroLinkSerializer
from core.filters.livro import LivroFiltro


class LivroLista(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    filterset_class = LivroFiltro
    search_fields = ('^nome',)
    ordering_fields = ('nome', 'data_publicacao')
    name = 'Livros cadastrados'

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return LivroSerializer
        return LivroLinkSerializer

class LivroDetalhe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer 
    name = 'Informações do livro'
