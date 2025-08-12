from django.shortcuts import render, redirect # Rendenização de templates e redirecionamento de URLs | Rendering templates and redirecting URLs
from usuarios.forms import LoginForms, CadastroForms # Importação dos formulários de login e cadastro | Importing login and registration forms
from django.contrib.auth.models import User #Módulo de usuário, responsável por gerenciar usuários | User module responsible for managing users
from django.contrib import auth # Módulo de autenticação, responsável por autenticar usuários | Authentication module responsible for user authentication
from django.contrib import messages #Módulos de mensagens | Messages module for displaying messages to users

def login(request): #Função de login com requisição HTTP | Login function with HTTP request
    form = LoginForms() #Instância vazia do formulário de login | Empty instance of the login form

    if request.method == 'POST': #Valida se a requisição foi enviada via POST | Validates if the request was sent via POST
        form = LoginForms(request.POST) #Instância do formulário de login com os dados enviados | Instance of the login form with the submitted data

        if form.is_valid(): #Valida se o formulário é válido, executa validações do forms.py | Validates if the form is valid
            nome = form['nome_login'].value() #Campos a serem validados | Fields to be validated
            senha = form['senha'].value() #.value é usado para acessar o valor do campo | .value is used to access the field value

        usuario = auth.authenticate( #Verifica se o usuário existe e autentica | Checks if the user exists and authenticates
            request, # Requisição HTTP, necessário para autenticação | HTTP request, necessary for authentication
            username=nome, #Campos a serem validados | Fields to be validated
            password=senha
        )
        if usuario is not None: #Valida se existe um usuário e se ele foi autenticado | Validates if a user exists and has been authenticated
            auth.login(request, usuario) #Módulo auth que efetua o login e vincula o user à sessão HTTP | Auth module that performs the login and binds the user to the HTTP session
            messages.success(request, f'{nome} logado com sucesso!') #Mensagem de sucesso do módulo messages | Success message from the messages module
            return redirect('exclusiva') #Redireciona para a página exclusiva após o login | Redirects to the exclusive page after login
        else:
            messages.error(request, 'Erro ao efetuar login') # Se der erro, exibe mensagem de erro | If an error occurs, displays an error message
            return redirect('login') #Redireciona para tentar o login novamente | Redirects to try logging in again

    return render(request, 'logiN/login.html', {'form': form}) #Renderiza o template de login com o formulário | Renders the login template with the form

# A lógica de cadastro segue o mesmo raciocínio do login
def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            nome=form['nome_cadastro'].value()
            email=form['email'].value()
            senha=form['senha_1'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já existente')
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, 'Cadastro efetuado com sucesso!')
            return redirect('login')

    return render(request, 'logiN/cadastro.html', {'form': form})

#A função de logout não entra no forms por que o forms é apenas para campos a serem preenchidos pelo usuário, enquanto o logout é uma ação que não requer campos adicionais

def logout(request): #A função recebe os dados do usuário logado | The function receives the logged-in user's data
    auth.logout(request) #Módulo auth que efetua o logout e desvincula o user da sessão HTTP | Auth module that performs the logout and unbinds the user from the HTTP session
    messages.success(request, 'Logout efetuado com sucesso!') #Mensagem de sucesso do módulo messages | Success message from the messages module
    return redirect('login') #Redireciona para a página de login após o logout | Redirects to the login page after logout