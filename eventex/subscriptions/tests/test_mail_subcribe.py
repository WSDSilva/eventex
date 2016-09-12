from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):

    def setUp(self):
        data = dict(nome='Wanderson Duarte', cpf='12345678901',
                    email='wsistemas.br@gmail.com', phone='21-999046793')

        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):

        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_emal_to(self):
        expect = ['contato@eventex.com.br', 'wsistemas.br@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_body(self):
        contets = ['Wanderson Duarte',
                   '12345678901',
                   'wsistemas.br@gmail.com',
                   '21-999046793']

        for content in contets:
            with self.subTest():
                self.assertIn(content, self.email.body)

