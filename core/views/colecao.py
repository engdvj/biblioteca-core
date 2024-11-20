from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from core.permisions.custom_permissions import IsColecionador
from rest_framework.authentication import TokenAuthentication
from core.models.colecao import Colecao
from core.serializers.colecao import ColecaoSerializer
from core.serializers.relacionados import ColecaoLinkSerializer# Importando ambos os serializers
from core.filters.colecao import ColecaoFiltro  # Certifique-se de que o filtro esteja definido

# View para listar e criar coleções, usando o serializer que mostra apenas links
class ColecaoLista(generics.ListCreateAPIView):
    queryset = Colecao.objects.prefetch_related('livros').all()
    serializer_class = ColecaoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filterset_class = ColecaoFiltro
    search_fields = ('^nome',)
    ordering_fields = ('nome',)

    def get_serializer_class(self):
        # Usa o serializer simplificado para listagem e completo para criação
        if self.request.method == 'POST':
            return ColecaoSerializer
        return ColecaoLinkSerializer

    def perform_create(self, serializer):
        # Define o colecionador como o usuário autenticado
        serializer.save(colecionador=self.request.user)

# View para detalhes de uma coleção específica
class ColecaoDetalhe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Colecao.objects.prefetch_related('livros').all()
    serializer_class = ColecaoSerializer
    permission_classes = [IsColecionador]
    authentication_classes = [TokenAuthentication]




