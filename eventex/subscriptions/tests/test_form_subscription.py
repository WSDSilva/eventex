from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):

    def test_form_has_fields(self):
        """Form must have 4 fields."""
        form = SubscriptionForm()
        expected = ['nome', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_is_digit(self):
        """"CPF must only accept digits."""
        form = self.make_validated_form(cpf='ABCD5678901')
        form.is_valid()

        # self.assertformerrormessage(form, 'cpf', 'O CPF deve conter apenas números')

        self.assertformerrorcode(form, 'cpf', 'digitos')
    def test_has_11_digits(self):
        """"CPF must have 11 digits."""
        form = self.make_validated_form(cpf='1234')

        self.assertformerrorcode(form, 'cpf', 'tamanho')

    def assertformerrorcode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]

        self.assertEqual(code, exception.code)


    def assertformerrormessage(self,form, field, msg):

        errors = form.errors
        errors_list = errors[field]

        self.assertEqual([msg], errors_list)


    def make_validated_form(self, **kwargs):
        valid = dict(nome='Wanderson Duarte', cpf='12345678901',
                    email='wandersonduarte.br@gmail.com', phone='21-999046793')

        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)

        form.is_valid()

        return form
