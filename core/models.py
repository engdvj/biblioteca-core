from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255, unique=True)
    publication_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=250, unique=True)
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)  # Verifique se o nome do campo é 'author'
    category = models.ForeignKey(Category, related_name="books", on_delete=models.CASCADE)
    publication_date = models.DateTimeField()
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
