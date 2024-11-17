from rest_framework import serializers
from core.models.categoria import Categoria
from core.serializers.livro import LivroSimplificadoSerializer

# Serializer para Categoria que exibe o nome e o link dos livros associados
class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    livros = LivroSimplificadoSerializer(many=True, read_only=True)

    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'livros']  # Inclui o nome e o URL dos livros
        extra_kwargs = {'url': {'view_name': 'categoria-detail'}}

# Serializer Reduzido para mostrar apenas o link da categoria
class CategoriaLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nome', 'url']  # Apenas o nome e o URL da categoria
        extra_kwargs = {'url': {'view_name': 'categoria-detail'}}
