from django.urls import include, path
from core import views

urlpatterns = [
    path('', views.ApiRaiz.as_view(), name='api-root'),  # Atualizado ApiRoot -> ApiRaiz
    path('livros/', views.LivroLista.as_view(), name='lista-livros'),
    path('livros/<int:pk>/', views.LivroDetalhe.as_view(), name='detalhe-livro'),
    path('autores/', views.AutorLista.as_view(), name='lista-autores'),
    path('autores/<int:pk>/', views.AutorDetalhe.as_view(), name='detalhe-autor'),
    path('categorias/', views.CategoriaLista.as_view(), name='lista-categorias'),
    path('categorias/<int:pk>/', views.CategoriaDetalhe.as_view(), name='detalhe-categoria'),
]
