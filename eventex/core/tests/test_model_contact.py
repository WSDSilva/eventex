from unittest import skip

from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact

class ContactModelTeste(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            nome='Henrinque Bastos',
            slug='henrique-bastos',
            photo='http://hbn.link/hb-pic')

    def test_email(self):
        contact = Contact.objects.create(
                    speaker = self.speaker,
                    kind = Contact.EMAIL,
                    value = 'henrique@bastos.net')

        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(
                    speaker = self.speaker,
                    kind = Contact.PHONE,
                    value = '21-996186180')

        self.assertTrue(Contact.objects.exists())

    def test_choice(self):
        """Contact kind should be limited to E or P"""
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='henrique@bastos.net')

        self.assertEqual('henrique@bastos.net', str(contact))


class ContactManagerTest(TestCase):

    def setUp(self):
        s = Speaker.objects.create(nome='Wanderson Duarte',
                                   slug='wanderson-duarte',
                                   photo='http://wsds-link/ws-pick')
        s.contact_set.create(kind=Contact.EMAIL, value='wsistemas.br@gmail.com')
        s.contact_set.create(kind=Contact.PHONE, value='21-999046793')

    def test_email(self):
        qs = Contact.objects.emails()
        expected = ['wsistemas.br@gmail.com']
        self.assertQuerysetEqual(qs,expected, lambda o: o.value)

    def test_phone(self):
        qs = Contact.objects.phones()
        expected = ['21-999046793']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)