from datetime import datetime

from django.shortcuts import resolve_url
from django.test import TestCase

from django_brazilian_addresses.addresses.models import State, City


class CityModelTest(TestCase):
    def setUp(self):
        state = State.objects.create(name='Paraná', initials='PR')
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

    def test_absolute_url(self):
        url = resolve_url('city-detail', self.city.pk)
        self.assertEqual(url, self.city.get_absolute_url())

    def test_get_state_name(self):
        self.assertEqual('Paraná', self.city.get_state_name())

    def test_create_date(self):
        """City must have an auto created_at attrs."""
        self.assertIsInstance(self.city.created_at, datetime)

    def test_update_date(self):
        """City must have an auto updated_at attrs."""
        self.assertIsInstance(self.city.updated_at, datetime)
