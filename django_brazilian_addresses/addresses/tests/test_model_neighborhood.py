from datetime import datetime

from django.shortcuts import resolve_url
from django.test import TestCase

from django_brazilian_addresses.addresses.models import State, City, \
    Neighborhood


class NeighborhoodModelTest(TestCase):
    def setUp(self):
        state = State.objects.create(name='Paraná', initials='PR')
        city = City.objects.create(name='Cascavel', state=state)
        self.neigh = Neighborhood.objects.create(
            name='Santa Felicidade', city=city)

    def test_create(self):
        self.assertTrue(Neighborhood.objects.exists())

    def test_str(self):
        self.assertEqual('Santa Felicidade', str(self.neigh))

    def test_absolute_url(self):
        url = resolve_url('neighborhood-detail', self.neigh.pk)
        self.assertEqual(url, self.neigh.get_absolute_url())

    def test_get_city_name(self):
        self.assertEqual('Cascavel', self.neigh.get_city_name())

    def test_create_date(self):
        """Neighborhood must have an auto created_at attrs."""
        self.assertIsInstance(self.neigh.created_at, datetime)

    def test_update_date(self):
        """Neighborhood must have an auto updated_at attrs."""
        self.assertIsInstance(self.neigh.updated_at, datetime)
