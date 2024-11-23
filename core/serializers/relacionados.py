from rest_framework import serializers
from core.models.livro import Livro
from core.models.autor import Autor
from core.models.categoria import Categoria
from core.models.colecao import Colecao

class AutorLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Autor
        fields = ['nome', 'url']
        extra_kwargs = {'url': {'view_name': 'autor-detail'}}

class CategoriaLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nome', 'url']
        extra_kwargs = {'url': {'view_name': 'categoria-detail'}}

class ColecaoLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Colecao
        fields = ['nome', 'url'] 
        extra_kwargs = {
            'url': {'view_name': 'colecao-detail', 'lookup_field': 'pk'}
        }

class LivroLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Livro
        fields = ['nome', 'url']
        extra_kwargs = {'url': {'view_name': 'livro-detail'}}
