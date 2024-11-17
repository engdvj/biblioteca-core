from rest_framework import serializers
from core.models.colecao import Colecao
from core.models.livro import Livro
from core.serializers.livro import LivroSimplificadoSerializer

# Serializer para Colecao que mostra o nome e o URL dos livros
class ColecaoSerializer(serializers.ModelSerializer):
    livros = LivroSimplificadoSerializer(many=True, read_only=True)

    class Meta:
        model = Colecao
        fields = ['id', 'nome', 'descricao', 'livros']

    def create(self, validated_data):
        # Associa automaticamente o usuário autenticado como o colecionador
        validated_data['colecionador'] = self.context['request'].user
        return super().create(validated_data)

# Serializer para mostrar apenas o link da coleção
class ColecaoLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Colecao
        fields = ['nome','url']  # Apenas o campo 'url'
        extra_kwargs = {'url': {'view_name': 'colecao-detail'}}



