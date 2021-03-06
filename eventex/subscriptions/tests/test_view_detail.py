import hashlib

from django.test import TestCase
from django.shortcuts import resolve_url as r
from django.core.urlresolvers import reverse
from eventex.subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):

    def setUp(self):
        self.obj = Subscription.objects.create(
            nome='Wanderon Duarte',
            cpf='12345678901',
            email='wsistemas.br@gmail.com',
            phone='21-999046793')
        self.resp = self.client.get(r('subscriptions:detail', self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

    def test_context(self):
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = (self.obj.nome, self.obj.cpf,
                    self.obj.email, self.obj.phone)

        with self.subTest():
            for expected in contents:
                self.assertContains(self.resp, expected)


class SubscriptionDetailNotFound(TestCase):
    def test_not_found(self):
        resp = self.client.get(r('subscriptions:detail', 0))
        self.assertEqual(404, resp.status_code)