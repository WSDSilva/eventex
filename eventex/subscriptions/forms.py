from django import forms
from django.core.exceptions import ValidationError

from eventex.subscriptions.models import Subscription
from eventex.subscriptions.validators import validate_cpf


class SubscriptionFormOld(forms.Form):
    nome = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF', validators=[validate_cpf])
    email = forms.EmailField(label='E-Mail', required=False)
    phone = forms.CharField(label='Telefone', required=False)

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        words = [w.capitalize() for w in nome.split()]

        return ' '.join(words)

    def clean(self):

        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu e-mail ou telefone')

        return self.cleaned_data


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['nome', 'cpf', 'email', 'phone']

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        words = [w.capitalize() for w in nome.split()]

        return ' '.join(words)


    def clean(self):
        self.cleaned_data = super().clean()

        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu e-mail ou telefone')

        return self.cleaned_data
