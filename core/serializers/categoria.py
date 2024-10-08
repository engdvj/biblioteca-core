from rest_framework import serializers
from core.models.categoria import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    livros = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='Informações do livro'
    )
    detalhe = serializers.HyperlinkedIdentityField(view_name='Informações da categoria')

    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'livros', 'detalhe']
