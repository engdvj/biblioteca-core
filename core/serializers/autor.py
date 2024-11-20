from rest_framework import serializers
from core.models.autor import Autor
from core.serializers.livro import LivroSimplificadoSerializer

# Serializer para Autor que exibe o nome e o link dos livros associados
class AutorSerializer(serializers.ModelSerializer):
    livros = LivroSimplificadoSerializer(many=True, read_only=True)

    class Meta:
        model = Autor
        fields = ['id', 'nome', 'livros']  # Exibe os livros associados
        extra_kwargs = {'url': {'view_name': 'autor-detail'}}

# Serializer Reduzido para mostrar apenas o link do autor
class AutorLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Autor
        fields = ['nome', 'url']  # Apenas o nome e o URL do autor
        extra_kwargs = {'url': {'view_name': 'autor-detail'}}
