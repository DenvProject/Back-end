from django.test import TestCase

# Create your tests here.
class DummyTest(TestCase):

    def test_dummy(self):
        self.assertEqual(True, True)

class AnotherDummyTest(TestCase):

    def test_dummy(self):
        self.assertEqual(True, True)