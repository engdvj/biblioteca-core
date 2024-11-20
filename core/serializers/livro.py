from rest_framework import serializers
from core.models.livro import Livro
from core.serializers.relacionados import AutorLinkSerializer, CategoriaLinkSerializer

class LivroSerializer(serializers.ModelSerializer):
    autor = AutorLinkSerializer(read_only=True)
    categoria = CategoriaLinkSerializer(read_only=True)

    class Meta:
        model = Livro
        fields = ['id', 'nome', 'autor', 'categoria', 'data_publicacao', 'publicado']
