from django.shortcuts import render
from produtos.models import Produto
from produtos.forms import UsuarioForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

def cadastro_usuario(request):
    if request.method == 'POST':
        forms = UsuarioForm(request.POST)
        if forms.is_valid():
            forms.save()
            forms = UsuarioForm()
    else:
        forms = UsuarioForm(  )
    return render (request, 'forms.html', {'form' : forms })


def base (request):
    return render(request, 'base.html')

#@login_required
def index(request):
	return render(request, 'index.html')

#@login_required
#def login (request):
#    return render(request, 'login.html')

def listagem(request):
	lista = Produto.objects.all()
	context = {'produtos' : lista}
	return render(request, 'listagem.html', context)

def detalhes(request, id):
	produto = Produto.objects.get(id=id)
	context={'produto': produto}
	return render(request, 'detalhes.html', context)

def quem_somos (request):
    return render(request, 'quemsomos.html')

@login_required
def sacola(request, id):
    produto = Produto.objects.get(id=id)
    context = {'produto':produto}
    return render(request, 'sacola.html',context)

#isso serve para deslogar, redireciona a página para login
#no caso ainda precisa inserir esse botão com url
def logout_aplicacao(request):
    logout(request)
    return redirect('login')