from rest_framework import serializers
from core.models.autor import Autor

class AutorSerializer(serializers.ModelSerializer):
    livros = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='detalhe-livro'
    )
    detalhe = serializers.HyperlinkedIdentityField(view_name='detalhe-autor')

    class Meta:
        model = Autor
        fields = ['id', 'nome', 'livros', 'detalhe']
