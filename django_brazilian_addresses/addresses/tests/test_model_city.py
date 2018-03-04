from datetime import datetime
from django.test import TestCase

from django_brazilian_addresses.addresses.models import Country, State, City


class CityModelTest(TestCase):
    def setUp(self):
        country = Country.objects.create(name='Brasil')
        state = State.objects.create(
            name='Paraná', initials='PR', country=country)
        self.city = City.objects.create(name='Cascavel', state=state)

    def test_create(self):
        self.assertTrue(City.objects.exists())

    def test_str(self):
        self.assertEqual('Cascavel', str(self.city))

    def test_zipcode_blank(self):
        """Cities zipcode can be blank"""
        field = City._meta.get_field('zipcode')
        self.assertTrue(field.blank)

    def test_zipcode_null(self):
        """Cities zipcode can be null"""
        field = City._meta.get_field('zipcode')
        self.assertTrue(field.null)

    def test_ibge_blank(self):
        """Ibge code can be blank"""
        field = City._meta.get_field('ibge')
        self.assertTrue(field.blank)

    def test_ibge_null(self):
        """Ibge code can be null"""
        field = City._meta.get_field('ibge')
        self.assertTrue(field.null)

    def test_create_date(self):
        """City must have an auto created_at attrs."""
        self.assertIsInstance(self.city.created_at, datetime)

    def test_update_date(self):
        """City must have an auto updated_at attrs."""
        self.assertIsInstance(self.city.updated_at, datetime)
