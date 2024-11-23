from rest_framework import serializers
from core.models.livro import Livro
from core.models.autor import Autor
from core.models.categoria import Categoria
from core.serializers.relacionados import AutorLinkSerializer, CategoriaLinkSerializer

class LivroSerializer(serializers.ModelSerializer):
    autor = AutorLinkSerializer(read_only=True)  
    categoria = CategoriaLinkSerializer(read_only=True) 
    autor_selecao = serializers.PrimaryKeyRelatedField(
        queryset=Autor.objects.all(), write_only=True, label="Autor"
    )
    categoria_selecao = serializers.PrimaryKeyRelatedField(
        queryset=Categoria.objects.all(), write_only=True, label="Categoria"
    ) 

    class Meta:
        model = Livro
        fields = [
            'id', 'nome', 'autor', 'categoria', 
            'autor_selecao', 'categoria_selecao', 
            'data_publicacao', 'publicado'
        ]

    def create(self, validated_data):
        autor = validated_data.pop('autor_selecao')
        categoria = validated_data.pop('categoria_selecao')
        livro = Livro.objects.create(autor=autor, categoria=categoria, **validated_data)
        return livro

    def update(self, instance, validated_data):
        autor = validated_data.pop('autor_selecao', None)
        categoria = validated_data.pop('categoria_selecao', None)
        if autor:
            instance.autor = autor
        if categoria:
            instance.categoria = categoria
        return super().update(instance, validated_data)
