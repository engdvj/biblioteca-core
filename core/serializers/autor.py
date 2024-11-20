from rest_framework import serializers
from core.models.autor import Autor
from core.serializers.relacionados import LivroLinkSerializer

class AutorSerializer(serializers.ModelSerializer):
    livros = LivroLinkSerializer(many=True, read_only=True)

    class Meta:
        model = Autor
        fields = ['id', 'nome', 'livros']
