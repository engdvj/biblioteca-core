from django.db import models
    
class Autor(models.Model):  # Atualizado o nome
    nome = models.CharField(max_length=255, unique=True)
    data_publicacao = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome

class Categoria(models.Model):  # Atualizado o nome
    nome = models.CharField(max_length=250, unique=True)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome

class Livro(models.Model):  # Atualizado o nome
    nome = models.CharField(max_length=250, unique=True)
    autor = models.ForeignKey(Autor, related_name="livros", on_delete=models.CASCADE)  # Atualizado para "autor"
    categoria = models.ForeignKey(Categoria, related_name="livros", on_delete=models.CASCADE)  # Atualizado para "categoria"
    data_publicacao = models.DateTimeField()
    publicado = models.BooleanField(default=False)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome