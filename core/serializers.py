from rest_framework import serializers
from .models import Author, Category, Book

class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='book-detail'
    )
    detail = serializers.HyperlinkedIdentityField(view_name='author-detail')

    class Meta:
        model = Author
        fields = ['id', 'name', 'books', 'detail']


class CategorySerializer(serializers.ModelSerializer):
    books = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='book-detail'
    )
    detail = serializers.HyperlinkedIdentityField(view_name='category-detail')

    class Meta:
        model = Category
        fields = ['id', 'name', 'books', 'detail']


class BookSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(view_name='book-detail')

    class Meta:
        model = Book
        fields = ['id', 'name', 'category', 'author', 'publication_date', 'is_published', 'detail']