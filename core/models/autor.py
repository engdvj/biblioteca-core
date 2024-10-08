from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    data_publicacao = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome
