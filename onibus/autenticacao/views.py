from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate,login,logout
from django.contrib import auth
from django.contrib.auth.decorators import login_required



def pag_cadastro(request):
    return render(request,'cadastrar.html')

def pag_logar(request):
    return render(request,'logar.html')


def cadastramento(request):
     if request.method== "GET":
         return render(request,'cadastrar.html')
     elif request.method== "POST":
         username=request.POST.get('username')
         email=request.POST.get('email')
         senha=request.POST.get('senha')

         if len(username.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/auth/cadastramento')
         user=User.objects.filter(username=username)
         user1=User.objects.filter(email=email)
         if  user.exists():
             messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse nome cadastrado')
             return redirect('cadastramento')
         if user1.exists():
             messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse email cadastrado')
             return redirect('cadastramento')
         
         try:
            # usu=Cliente(usuario=username)
            # usu.save()
            user = User.objects.create_user( username=username, email=email, password=senha)
            messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso')
            return redirect('pag_logar')

         except:
            return redirect('pag_cadastro')
         
        #  return HttpResponse('pass')




def logar(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            messages.add_message(request, constants.ERROR, 'Já há um usuario logado')
            return redirect('pag_logar')
        return render(request, 'logar.html')
    elif request.method == "POST":
        if request.user.is_authenticated:
            messages.add_message(request, constants.ERROR, 'Já há um usuario logado')
            return redirect('pag_logar')
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        print(username)
        print(senha)
        usuario = authenticate(username=username, password=senha)
        print(usuario)
        if not usuario:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos')
            return redirect('/auth/logar')
        else:
            login(request, usuario)
            return redirect('/')

@login_required
def deslogar(request):
    logout(request)
    messages.add_message(request, constants.SUCCESS, 'Usuario logout')
    return redirect('pag_logar')