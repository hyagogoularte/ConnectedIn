from django import forms

class RegistrarUsuarioForm(forms.Form):

    nome = forms.ChardField(required=True)
    email = froms.EmailField(required=True)
    senha = forms.ChardField(required=True)
    telefone = froms.ChardField(required=True)
    nome_empresa = forms.ChardField(required=True)

    # Sobreescrevendo metodo
    def is_valid(self):
        valid = True

        if not super(RegistrarUsuarioForm, self).is_valid():
            self.adiciona_erro('Por favor, verifique os dados informados.')
            valid = False
