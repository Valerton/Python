from django.test import TestCase
from ventochell.models import Event


class EventTestCase(TestCase):
    def setUp(self):
        Event.objects.create(name="test_1", location="test_2", date="test_3", creator="test_4", img="test_5", description="test_6")

    def test_rate(self):
        user = Event.objects.get(name="test_1")
        self.assertEqual(user.location, "test_2")
        self.assertEqual(user.date, "test_3")
        self.assertEqual(user.creator, "test_4")
        self.assertEqual(user.img, "test_5")
        self.assertEqual(user.description, "test_6")
