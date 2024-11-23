from rest_framework import serializers
from core.models.colecao import Colecao
from core.models.livro import Livro
from core.serializers.relacionados import LivroLinkSerializer

class ColecaoSerializer(serializers.ModelSerializer):
    livros = LivroLinkSerializer(many=True, read_only=True) 
    livros_selecao = serializers.PrimaryKeyRelatedField(
        queryset=Livro.objects.all(), many=True, write_only=True, label="Livros" 
    )

    class Meta:
        model = Colecao
        fields = ['id', 'nome', 'descricao', 'livros', 'livros_selecao']

    def create(self, validated_data):
        livros = validated_data.pop('livros_selecao', [])
        colecao = Colecao.objects.create(**validated_data)
        colecao.livros.set(livros)
        return colecao

    def update(self, instance, validated_data):
        livros = validated_data.pop('livros_selecao', [])
        instance = super().update(instance, validated_data)
        instance.livros.set(livros)
        return instance
