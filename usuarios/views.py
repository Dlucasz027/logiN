from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


def login(request):
    if request.method == 'POST':
        login_form = LoginForms(request.POST)

        if login_form.is_valid():
            nome = login_form.cleaned_data['nome_login']
            senha = login_form.cleaned_data['senha']

            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha
            )
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f'{nome} logado com sucesso!')
                return redirect('exclusiva')
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
                return render(request, 'logiN/index.html', {'form': login_form})

    else:
        login_form = LoginForms()

    return render(request, 'logiN/index.html', {'form': login_form})


def cadastro(request):
    if request.method == 'POST':
        cadastro_form = CadastroForms(request.POST)

        if cadastro_form.is_valid():
            nome = cadastro_form.cleaned_data['nome_cadastro']
            email = cadastro_form.cleaned_data['email']
            senha = cadastro_form.cleaned_data['senha_1']

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já existente')
                return render(request, 'logiN/cadastro.html', {'form': cadastro_form})

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, 'Cadastro efetuado com sucesso! Faça seu login.')
            return redirect('login')

    else:
        cadastro_form = CadastroForms()

    return render(request, 'logiN/cadastro.html', {'form': cadastro_form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')