from django import forms #Importa o módulo forms do Django que por padrão contém configurações de formulários | Import the forms module from Django which contains form configurations by default

class LoginForms(forms.Form): #Classe que define o formulário de login | Class that defines the login form
    nome_login=forms.CharField(  #Método que define o campo de nome de login | Method that defines the login name field
        label='Nome de Login', 
        required=True, 
        max_length=100,
        widget=forms.TextInput( #widget define o tipo de campo como texto | widget defines the field type as text
            attrs={  #Atributos do campo de nome de login, sem eles o campo não será exibido corretamente | Attributes of the login name field, without them the field will not be displayed correctly
                'class': 'form-control',
                'placeholder': 'Ex.: João Silva',
            }
        )
    )
    senha=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',
            }
        ),
    )

class CadastroForms(forms.Form): #Vamos seguir o mesmo padrão do formulário de login, mas com campos diferentes | We will follow the same pattern as the login form, but with different fields
    nome_cadastro=forms.CharField(
        label='Nome de Cadastro', 
        required=True, 
        max_length=100,
        widget=forms.TextInput( #Campo de texto simples | Simple text field
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João Silva',
            }
        )
    )
    email=forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput( #Campo com configuração de email, vem do import forms.EmailField | Field with email configuration, comes from the import forms.EmailField
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: joaosilva@xpto.com',
            }
        )
    )
    senha_1=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput( #Campo com configuração de senha, vem do import forms.CharField | Field with password configuration, comes from the import forms.CharField
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',
            }
        ),
    )
    senha_2=forms.CharField(
        label='Confirme a sua senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha novamente',
            }
        ),
    )

    def clean_nome_cadastro(self): #Método para validar o campo nome_cadastro | Method to validate the nome_cadastro field
        nome = self.cleaned_data.get('nome_cadastro') #.cleaned_data é um dicionário que contém os dados limpos do formulário | .cleaned_data is a dictionary that contains the cleaned data of the form

        if nome:
            nome = nome.strip() #Strip remove espaços em branco no início e no final da string | strip removes whitespace from the beginning and end of the string
            if ' ' in nome:
                raise forms.ValidationError('Espaços não são permitidos nesse campo')
            else:
                return nome

    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('Senhas não são iguais')# Raise é como se fosse um alarme que dispara quando algo está errado | Raise is like an alarm that goes off when something is wrong
            else:
                return senha_2