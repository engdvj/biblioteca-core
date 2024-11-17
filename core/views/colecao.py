from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from core.permisions.custom_permissions import IsColecionador
from rest_framework.authentication import TokenAuthentication
from core.models.colecao import Colecao
from core.serializers.colecao import ColecaoSerializer, ColecaoLinkSerializer  # Importando ambos os serializers
from core.filters.colecao import ColecaoFiltro  # Certifique-se de que o filtro esteja definido

# View para listar e criar coleções, usando o serializer que mostra apenas links
class ColecaoLista(generics.ListCreateAPIView):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer  # Use ColecaoSerializer para criar coleções
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filterset_class = ColecaoFiltro
    search_fields = ('^nome',)
    ordering_fields = ('nome',)

    def perform_create(self, serializer):
        # Passa o usuário autenticado ao criar a coleção
        serializer.save(colecionador=self.request.user)

# View para detalhes de uma coleção específica
class ColecaoDetalhe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    permission_classes = [IsColecionador] 
