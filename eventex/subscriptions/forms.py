from django import forms

class SubscriptionForm(forms.Form):
    nome = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF')
    email = forms.EmailField(label='E-Mail')
    phone = forms.CharField(label='Telefone')