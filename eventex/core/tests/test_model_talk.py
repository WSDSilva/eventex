from django.test import TestCase

from eventex.core.models import Talk


class ModelTalkTest(TestCase):

    def setUp(self):
        self.talk = Talk.objects.create(
            title='Título da palestra',
            start='10:00',
            description='Descrição da palestra'
        )


    def test_create(self):
        self.assertTrue(Talk.objects.exists())

    def test_has_speakers(self):
        """Talk has many Speakers and vice-versa"""
        self.talk.speakers.create(
            nome='Henrique Bastos',
            slug='henrique-bastos',
            website='http://henriquebastos.net'
        )

        self.assertEqual(1, self.talk.speakers.count())


    def test_description_blank(self):
        field = Talk._meta.get_field('description')
        self.assertTrue(field.blank)

    def test_speaker_blank(self):
        field = Talk._meta.get_field('speakers')
        self.assertTrue(field.blank)

    def test_start_blank(self):
        field = Talk._meta.get_field('start')
        self.assertTrue(field.blank)

    def test_start_null(self):
        field = Talk._meta.get_field('start')
        self.assertTrue(field.null)

    def test_str(self):
        self.assertEqual('Título da palestra', str(self.talk.title))