from rest_framework import serializers
from core.models.livro import Livro

# Serializer para Livro que mostra links para autor e categoria
class LivroSerializer(serializers.HyperlinkedModelSerializer):
    autor = serializers.HyperlinkedRelatedField(
        view_name='autor-detail',
        read_only=True
    )
    categoria = serializers.HyperlinkedRelatedField(
        view_name='categoria-detail',
        read_only=True
    )

    class Meta:
        model = Livro
        fields = ['id', 'nome', 'autor', 'categoria', 'data_publicacao', 'publicado']
        extra_kwargs = {'url': {'view_name': 'livro-detail'}}

# Serializer Reduzido para mostrar apenas o link do livro
class LivroLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Livro
        fields = ['nome','url']  # Apenas o campo 'url'
        extra_kwargs = {'url': {'view_name': 'livro-detail'}}
        
        
class LivroSimplificadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Livro
        fields = ['nome', 'url']  # Inclui apenas o nome e o URL
        extra_kwargs = {'url': {'view_name': 'livro-detail'}}