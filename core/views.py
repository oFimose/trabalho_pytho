from django.shortcuts import render, redirect
from django import forms
from .models import Produto, Categoria

# Home view
def home(request):
    return render(request, 'home.html')

# Formulário de produto
class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'estoque', 'categoria']

    descricao = forms.CharField(widget=forms.Textarea(attrs={'rows': 3,'cols': 50}))
def cadastro_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o produto no banco de dados
            return redirect('home')  # Redireciona para a página inicial ou outra página
        else:
            print(form.errors)
    else:
        form = ProdutoForm()

    return render(request, 'cadastro_produto.html', {'form': form})

# Formulário de categoria
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao']

def cadastro_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()  # Salva a categoria no banco de dados
            return redirect('home')  # Redireciona para a página inicial ou outra página
        else:
            print(form.errors)  # Exibe os erros no console se o formulário não for válido
    else:
        form = CategoriaForm()

    return render(request, 'cadastro_categoria.html', {'form': form})

def home(request):
    produtos = Produto.objects.all()
    return render(request, 'home.html', {'produtos': produtos})

def editar_produto(request, id):
    produto = Produto.objects.get(id=id)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'cadastro_produto.html', {'form': form})

def deletar_produto(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect('home')

