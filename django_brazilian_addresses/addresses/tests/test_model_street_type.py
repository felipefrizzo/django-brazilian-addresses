from datetime import datetime
from django.test import TestCase

from django_brazilian_addresses.addresses.models import StreetType


class StreetTypeModelTest(TestCase):
    def setUp(self):
        self.street_type = StreetType.objects.create(name='Rua')

    def test_create(self):
        self.assertTrue(StreetType.objects.exists())

    def test_str(self):
        self.assertEqual('Rua', str(self.street_type))

    def test_abbreviation_blank(self):
        """Abbreviation can be blank"""
        field = StreetType._meta.get_field('abbreviation')
        self.assertTrue(field.blank)

    def test_abbreviation_null(self):
        """Abbreviation can be null"""
        field = StreetType._meta.get_field('abbreviation')
        self.assertTrue(field.null)

    def test_create_date(self):
        """Street Type must have an auto created_at attrs."""
        self.assertIsInstance(self.street_type.created_at, datetime)

    def test_update_date(self):
        """Street Type must have an auto updated_at attrs."""
        self.assertIsInstance(self.street_type.updated_at, datetime)
