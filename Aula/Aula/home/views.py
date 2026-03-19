from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro

def home(request):
    return render(request, 'home.html')


def cadastro(request):
    if request.method == 'POST':
        Livro.objects.create(
            titulo=request.POST['titulo'],
            autor=request.POST['autor'],
            editora=request.POST['editora'],
            ano=request.POST['ano'],
            paginas=request.POST['paginas'],
            categoria=request.POST['categoria'],
            isbn=request.POST['isbn'],
            idioma=request.POST['idioma'],
            descricao=request.POST['descricao'],
            cadastrado_por=request.POST['cadastrado_por']
        )
        return redirect('confirmacao')

    return render(request, 'cadastro.html')


def confirmacao(request):
    return render(request, 'confirmacao.html')


def consulta(request):
    if request.method == 'POST':
        nome = request.POST['titulo']
        livros = Livro.objects.filter(titulo__icontains=nome)
        return render(request, 'resultado_consulta.html', {'livros': livros})

    return render(request, 'consulta.html')


def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'listar_livros.html', {'livros': livros})


def detalhes_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    return render(request, 'detalhes_livro.html', {'livro': livro})


def excluir_livro(request, id):
    livro = get_object_or_404(Livro, id=id)

    if request.method == 'POST':
        livro.delete()
        return redirect('listar_livros')

    return render(request, 'confirmar_exclusao.html', {'livro': livro})


def sobre(request):
    return render(request, 'sobre.html')


def contato(request):
    return render(request, 'contato.html')