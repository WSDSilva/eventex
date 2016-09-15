from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscriptionModelTest(TestCase):

    def setUp(self):
        self.obj = Subscription(
            nome='Wanderson Duarte',
            cpf='12345678901',
            email='wsistemas.br@gmail.com',
            phone='21-999046793'
        )

        self.obj.save()


    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_create_at(self):
        """Subscription must have an auto craate_at attr."""
        self.assertIsInstance(self.obj.create_at, datetime)