from django_filters import rest_framework as filters
from .models import Book, Author, Category

class BookFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')  # Filtro pelo nome do livro (contém)
    author = filters.CharFilter(field_name='author__name', lookup_expr='icontains')  # Certifique-se de que o campo no modelo é 'author'
    category = filters.AllValuesFilter(field_name='category__name')  # Filtro pelo nome da categoria

    class Meta:
        model = Book
        fields = ['name', 'author', 'category', 'is_published']

# Filtro personalizado para autores
class AuthorFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Author
        fields = ['name']

# Filtro personalizado para categorias
class CategoryFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')  # Filtro pelo nome da categoria (contém)

    class Meta:
        model = Category
        fields = ['name']
