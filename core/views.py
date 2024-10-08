from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Autor, Livro, Categoria
from .serializers import AutorSerializer, LivroSerializer, CategoriaSerializer
from .filters import LivroFiltro, AutorFiltro, CategoriaFiltro  # Importando os novos filtros

# View para listar e criar livros
class LivroLista(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filterset_class = LivroFiltro  # Utilizando o filtro personalizado para livros
    search_fields = ('^nome',)  # Pesquisar pelo nome do livro (inicial com "^")
    ordering_fields = ('nome', 'data_publicacao')  # Ordenação pelo nome e data de publicação
    name = 'lista-livros'

# View para detalhar, atualizar e deletar livros
class LivroDetalhe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = 'detalhe-livro'

# View para listar e criar autores
class AutorLista(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    filterset_class = AutorFiltro  # Utilizando o filtro personalizado para autores
    search_fields = ('^nome',)  # Pesquisa pelo nome
    ordering_fields = ('nome',)  # Ordenação por nome
    name = 'lista-autores'

# View para detalhar, atualizar e deletar autores
class AutorDetalhe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = 'detalhe-autor'

# View para listar e criar categorias
class CategoriaLista(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filterset_class = CategoriaFiltro  # Utilizando o filtro personalizado para categorias
    search_fields = ('^nome',)  # Pesquisar categorias pelo nome
    ordering_fields = ('nome',)  # Ordenação pelo nome
    name = 'lista-categorias'

# View para detalhar, atualizar e deletar categorias
class CategoriaDetalhe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = 'detalhe-categoria'

# View para a raiz da API, mostrando os endpoints principais
class ApiRaiz(APIView):
    name = "Biblioteca API - Endpoints Principais"

    def get(self, request, *args, **kwargs):
        context = {
            "Listas": [
                {
                    "nome": "Autores",
                    "endpoint": reverse('lista-autores', request=request),
                    "descrição": "Lista todos os autores."
                },
                {
                    "nome": "Livros",
                    "endpoint": reverse('lista-livros', request=request),
                    "descrição": "Lista todos os livros."
                },
                {
                    "nome": "Categorias",
                    "endpoint": reverse('lista-categorias', request=request),
                    "descrição": "Lista todas as categorias."
                }
            ],
            "Detalhes": [
                {
                    "nome": "Autor",
                    "endpoint": "/api/autores/{id}/",
                    "descrição": "Obtém, atualiza ou deleta um autor específico pelo ID."
                },
                {
                    "nome": "Livro",
                    "endpoint": "/api/livros/{id}/",
                    "descrição": "Obtém, atualiza ou deleta um livro específico pelo ID."
                },
                {
                    "nome": "Categoria",
                    "endpoint": "/api/categorias/{id}/",
                    "descrição": "Obtém, atualiza ou deleta uma categoria específica pelo ID."
                }
            ]
        }
        return Response(context)
