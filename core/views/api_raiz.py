from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.urls import reverse

class ApiRaiz(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Gera os links para as listas de livros, autores e coleções
        autores_link = request.build_absolute_uri(reverse('autores-lista'))
        livros_link = request.build_absolute_uri(reverse('livros-lista'))
        categorias_link = request.build_absolute_uri(reverse('categorias-lista'))
        colecoes_link = request.build_absolute_uri(reverse('colecoes-lista'))

        return Response({
            "autores": autores_link,
            "livros": livros_link,
            "categorias": categorias_link,
            "minhas coleções": colecoes_link
        })
