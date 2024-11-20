from rest_framework import serializers
from core.models.colecao import Colecao
from core.models.livro import Livro
from core.serializers.livro import LivroSimplificadoSerializer

# Serializer para Colecao que mostra o nome e o URL dos livros
class ColecaoSerializer(serializers.ModelSerializer):
    livros = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Livro.objects.all()
    )

    class Meta:
        model = Colecao
        fields = ['id', 'nome', 'descricao', 'livros']  # Inclua os livros no serializer

    def create(self, validated_data):
        # Extrai os livros do payload
        livros = validated_data.pop('livros', [])
        colecao = Colecao.objects.create(**validated_data)
        colecao.livros.set(livros)  # Relaciona os livros à coleção
        return colecao

# Serializer para mostrar apenas o link da coleção
class ColecaoLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Colecao
        fields = ['nome','url']  # Apenas o campo 'url'
        extra_kwargs = {'url': {'view_name': 'colecao-detail'}}



