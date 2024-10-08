from rest_framework import generics
from core.models.livro import Livro
from core.serializers.livro import LivroSerializer
from core.filters.livro import LivroFiltro


class LivroLista(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filterset_class = LivroFiltro
    search_fields = ('^nome',)
    ordering_fields = ('nome', 'data_publicacao')
    name = 'Livros cadastrados'

class LivroDetalhe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = 'Informações do livro'
