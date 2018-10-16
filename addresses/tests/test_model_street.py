from datetime import datetime

from django.shortcuts import resolve_url
from django.test import TestCase

from addresses.models import State, City, Neighborhood, Street


class StreetModelTest(TestCase):
    def setUp(self):
        state = State.objects.create(name='Paraná', initials='PR')
        city = City.objects.create(name='Cascavel', state=state)
        neigh = Neighborhood.objects.create(name='Santa Felicidade', city=city)

        self.street = Street.objects.create(
            name='Rua João Ribeiro Pinheiro',
            zipcode='85803260', neighborhood=neigh
        )

    def test_create(self):
        self.assertTrue(Street.objects.exists())

    def test_str(self):
        self.assertEqual('Rua João Ribeiro Pinheiro', str(self.street))

    def test_get_state_initials(self):
        self.assertEqual('PR', self.street.get_state_initials())

    def test_get_city_name(self):
        self.assertEqual('Cascavel', self.street.get_city_name())

    def test_get_neighborhood_name(self):
        self.assertEqual(
            'Santa Felicidade', self.street.get_neighborhood_name())

    def test_absolute_url(self):
        url = resolve_url('street-detail', self.street.pk)
        self.assertEqual(url, self.street.get_absolute_url())

    def test_create_date(self):
        """Street must have an auto created_at attrs."""
        self.assertIsInstance(self.street.created_at, datetime)

    def test_update_date(self):
        """Street must have an auto updated_at attrs."""
        self.assertIsInstance(self.street.updated_at, datetime)


class StreetModelTestZipcodeIsNone(TestCase):
    def setUp(self):
        state = State.objects.create(name='Paraná', initials='PR')
        city = City.objects.create(
            name='Santa Tereza', state=state, zipcode='85825000')
        neigh = Neighborhood.objects.create(name='Centro', city=city)

        self.street = Street.objects.create(
            name='Avenida Paraná', neighborhood=neigh)

    def test_create(self):
        self.assertTrue(Street.objects.exists())

    def test_zipcode_get_from_city(self):
        """
        When the street do not have zipcode
        by default take the zipcode of the city.
        """
        self.assertEqual(
            self.street.neighborhood.city.zipcode, self.street.zipcode)
