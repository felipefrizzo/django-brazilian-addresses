from datetime import datetime

from django.shortcuts import resolve_url
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

    def test_get_state_initials(self):
        self.assertEqual('Brasil', self.state.get_country_name())

    def test_absolute_url(self):
        url = resolve_url('state-detail', self.state.pk)
        self.assertEqual(url, self.state.get_absolute_url())

    def test_create_date(self):
        """State must have an auto created_at attrs."""
        self.assertIsInstance(self.state.created_at, datetime)

    def test_update_date(self):
        """State must have an auto updated_at attrs."""
        self.assertIsInstance(self.state.updated_at, datetime)
