from rest_framework import serializers
from core.models.livro import Livro
from core.models.autor import Autor
from core.models.categoria import Categoria

# Serializer para Livro que mostra links para autor e categoria
class LivroSerializer(serializers.ModelSerializer):
    autor = serializers.PrimaryKeyRelatedField(
        queryset=Autor.objects.all()  # Permite selecionar o autor por ID
    )
    categoria = serializers.PrimaryKeyRelatedField(
        queryset=Categoria.objects.all()  # Permite selecionar a categoria por ID
    )

    class Meta:
        model = Livro
        fields = ['id', 'nome', 'autor', 'categoria', 'data_publicacao', 'publicado']

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