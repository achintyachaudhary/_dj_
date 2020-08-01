from django.test import TestCase


class DummyTest(TestCase):

    def setUp(self):
        pass

    def test_sample(self):
        self.assertEqual(5, 5)
