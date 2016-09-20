from django import forms
from django.core.exceptions import ValidationError


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('O CPF deve conter apenas números', 'digitos')

    if len(value) < 11:
        raise ValidationError('O CPF deve conter 11 dígitos', 'tamanho')

class SubscriptionForm(forms.Form):
    nome = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF', validators=[validate_cpf])
    email = forms.EmailField(label='E-Mail')
    phone = forms.CharField(label='Telefone')

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        words = [w.capitalize() for w in nome.split()]

        return ' '.join(words)