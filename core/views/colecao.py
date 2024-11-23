from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from core.permisions.custom_permissions import IsColecionador
from rest_framework.authentication import TokenAuthentication
from core.models.colecao import Colecao
from core.serializers.colecao import ColecaoSerializer
from core.serializers.relacionados import ColecaoLinkSerializer
from core.filters.colecao import ColecaoFiltro  


class ColecaoLista(generics.ListCreateAPIView):
    queryset = Colecao.objects.prefetch_related('livros').all()
    serializer_class = ColecaoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filterset_class = ColecaoFiltro
    search_fields = ('^nome',)
    ordering_fields = ('nome',)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ColecaoSerializer
        return ColecaoLinkSerializer

    def perform_create(self, serializer):
        serializer.save(colecionador=self.request.user)

class ColecaoDetalhe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Colecao.objects.prefetch_related('livros').all()
    serializer_class = ColecaoSerializer
    permission_classes = [IsColecionador]
    authentication_classes = [TokenAuthentication]




