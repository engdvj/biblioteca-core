from rest_framework import generics
from core.models.livro import Livro
from core.serializers.livro import LivroSerializer
from core.serializers.relacionados import LivroLinkSerializer
from core.filters.livro import LivroFiltro

# View para listar e criar livros, usando o serializer que mostra apenas links
class LivroLista(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    filterset_class = LivroFiltro
    search_fields = ('^nome',)
    ordering_fields = ('nome', 'data_publicacao')
    name = 'Livros cadastrados'

    def get_serializer_class(self):
        # Usa o serializer completo para criação
        if self.request.method == 'POST':
            return LivroSerializer
        return LivroLinkSerializer

# View para detalhes de um livro específico
class LivroDetalhe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer  # Usando o serializer completo para detalhes
    name = 'Informações do livro'
