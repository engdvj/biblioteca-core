from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Author, Book, Category
from .serializers import AuthorSerializer, BookSerializer, CategorySerializer
from .filters import BookFilter, AuthorFilter, CategoryFilter  # Importando os novos filtros


# View para listar e criar livros
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter  # Utilizando o filtro personalizado para livros
    search_fields = ('^name',)  # Pesquisar pelo nome do livro (inicial com "^")
    ordering_fields = ('name', 'publication_date')  # Ordenação pelo nome e data de publicação

# View para detalhar, atualizar e deletar livros
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'book-detail'

class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filterset_fields = ('name',)  # Atualizado para apenas o nome
    search_fields = ('^name',)  # Pesquisa pelo nome
    ordering_fields = ('name',)  # Ordenação por nome

# View para detalhar, atualizar e deletar autores
class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    name = 'author-detail'

# View para listar e criar categorias
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_class = CategoryFilter  # Utilizando o filtro personalizado para categorias
    search_fields = ('^name',)  # Pesquisar categorias pelo nome
    ordering_fields = ('name',)  # Ordenação pelo nome

# View para detalhar, atualizar e deletar categorias
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-detail'

class ApiRoot(APIView):
    def get(self, request, *args, **kwargs):
        context = {
            'authors': reverse('author-list', request=request),
            'books': reverse('book-list', request=request),
            'categories': reverse('category-list', request=request)
        }
        return Response(context)
