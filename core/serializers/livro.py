from rest_framework import serializers
from core.models.livro import Livro

class LivroSerializer(serializers.ModelSerializer):
    detalhe = serializers.HyperlinkedIdentityField(view_name='Informações do livro')

    class Meta:
        model = Livro
        fields = ['id', 'nome', 'categoria', 'autor', 'data_publicacao', 'publicado', 'detalhe']
