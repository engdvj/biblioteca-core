from django.db import models
from core.models.autor import Autor
from core.models.categoria import Categoria

class Livro(models.Model):
    nome = models.CharField(max_length=250, unique=True)
    autor = models.ForeignKey(Autor, related_name="livros", on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, related_name="livros", on_delete=models.CASCADE)
    data_publicacao = models.DateTimeField()
    publicado = models.BooleanField(default=False)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome
