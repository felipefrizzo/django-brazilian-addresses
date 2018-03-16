from datetime import datetime

from django.shortcuts import resolve_url
from django.test import TestCase

from django_brazilian_addresses.addresses.models import Country


class CountryModelTest(TestCase):
    def setUp(self):
        self.country = Country.objects.create(name='Brasil')

    def test_create(self):
        self.assertTrue(Country.objects.exists())

    def test_str(self):
        self.assertEqual('Brasil', str(self.country))

    def test_absolute_url(self):
        url = resolve_url('country-detail', self.country.pk)
        self.assertEqual(url, self.country.get_absolute_url())

    def test_create_date(self):
        """Country must have an auto created_at attrs."""
        self.assertIsInstance(self.country.created_at, datetime)

    def test_update_date(self):
        """Country must have an auto updated_at attrs."""
        self.assertIsInstance(self.country.updated_at, datetime)
