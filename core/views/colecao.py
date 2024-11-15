from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from core.models.colecao import Colecao
from core.serializers.colecao import ColecaoSerializer
from core.permisions.custom_permissions import IsColecionador


class ColecaoLista(generics.ListCreateAPIView):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    authentication_classes = [TokenAuthentication]  # Adiciona autenticação baseada em Token
    permission_classes = [IsAuthenticated]  # Apenas usuários autenticados podem visualizar ou criar
    name = 'Coleções cadastradas'

class ColecaoDetalhe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    authentication_classes = [TokenAuthentication]  # Adiciona autenticação baseada em Token
    permission_classes = [IsColecionador]  # Apenas o colecionador pode modificar ou deletar
    name = 'Informações da coleção'
