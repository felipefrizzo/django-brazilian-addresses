from datetime import datetime
from django.test import TestCase

from django_brazilian_addresses.addresses.models import Country, State


class StateModelTest(TestCase):
    def setUp(self):
        country = Country.objects.create(name='Brasil')
        self.state = State.objects.create(
            name='Paraná', initials='PR', country=country)

    def test_create(self):
        self.assertTrue(State.objects.exists())

    def test_str(self):
        self.assertEqual('Paraná', str(self.state))

    def test_create_date(self):
        """State must have an auto created_at attrs."""
        self.assertIsInstance(self.state.created_at, datetime)

    def test_update_date(self):
        """State must have an auto updated_at attrs."""
        self.assertIsInstance(self.state.updated_at, datetime)
