from rest_framework import serializers
from core.models.categoria import Categoria
from core.serializers.relacionados import LivroLinkSerializer

class CategoriaSerializer(serializers.ModelSerializer):
    livros = LivroLinkSerializer(many=True, read_only=True)

    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'livros']
