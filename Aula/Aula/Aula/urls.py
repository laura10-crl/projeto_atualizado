from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('confirmacao/', views.confirmacao, name='confirmacao'),
    path('consulta/', views.consulta, name='consulta'),
    path('listar/', views.listar_livros, name='listar_livros'),
    path('livro/<int:id>/', views.detalhes_livro, name='detalhes_livro'),
    path('excluir/<int:id>/', views.excluir_livro, name='excluir_livro'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
]