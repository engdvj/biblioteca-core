from rest_framework import serializers
from .models import Autor, Categoria, Livro

class AutorSerializer(serializers.ModelSerializer):
    livros = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='detalhe-livro'
    )
    detalhe = serializers.HyperlinkedIdentityField(view_name='detalhe-autor')

    class Meta:
        model = Autor  # Atualizado
        fields = ['id', 'nome', 'livros', 'detalhe']  # name -> nome

class CategoriaSerializer(serializers.ModelSerializer):
    livros = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='detalhe-livro'
    )
    detalhe = serializers.HyperlinkedIdentityField(view_name='detalhe-categoria')

    class Meta:
        model = Categoria  # Atualizado
        fields = ['id', 'nome', 'livros', 'detalhe']  # name -> nome

class LivroSerializer(serializers.ModelSerializer):
    detalhe = serializers.HyperlinkedIdentityField(view_name='detalhe-livro')

    class Meta:
        model = Livro  # Atualizado
        fields = ['id', 'nome', 'categoria', 'autor', 'data_publicacao', 'publicado', 'detalhe']  # name -> nome, category -> categoria, etc.
