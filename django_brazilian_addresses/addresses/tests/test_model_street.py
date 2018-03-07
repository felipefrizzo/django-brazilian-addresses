from datetime import datetime

from django.test import TestCase

from django_brazilian_addresses.addresses.models import Country, State, City, \
    Neighborhood, StreetType, Street


class StreetModelTest(TestCase):
    def setUp(self):
        country = Country.objects.create(name='Brasil')
        state = State.objects.create(
            name='Paraná', initials='PR', country=country)
        city = City.objects.create(name='Cascavel', state=state)
        neigh = Neighborhood.objects.create(name='Santa Felicidade', city=city)
        street_type = StreetType.objects.create(name='Rua')

        self.street = Street.objects.create(
            name='João Ribeiro Pinheiro', zipcode='85803260',
            neighborhood=neigh, street_type=street_type
        )

    def test_create(self):
        self.assertTrue(Street.objects.exists())

    def test_str(self):
        self.assertEqual('Rua João Ribeiro Pinheiro', str(self.street))

    def test_default_value_is_grand_user(self):
        """The Field is_grand_user by default will be False."""
        self.assertEqual(False, self.street.is_grand_user)

    def test_get_patio_type_name(self):
        self.assertEqual('Rua', self.street.get_street_type())

    def test_create_date(self):
        """Street must have an auto created_at attrs."""
        self.assertIsInstance(self.street.created_at, datetime)

    def test_update_date(self):
        """Street must have an auto updated_at attrs."""
        self.assertIsInstance(self.street.updated_at, datetime)


class StreetModelTestZipcodeIsNone(TestCase):
    def setUp(self):
        country = Country.objects.create(name='Brasil')
        state = State.objects.create(
            name='Paraná', initials='PR', country=country)
        city = City.objects.create(
            name='Santa Tereza', state=state, zipcode='85825000')
        neigh = Neighborhood.objects.create(name='Centro', city=city)
        street_type = StreetType.objects.create(name='Avenida')

        self.street = Street.objects.create(
            name='Paraná', neighborhood=neigh, street_type=street_type)

    def test_create(self):
        self.assertTrue(Street.objects.exists())

    def test_zipcode_get_from_city(self):
        """
        When the street do not have zipcode by default take the zipcode of the city.
        """
        self.assertEqual(
            self.street.neighborhood.city.zipcode, self.street.zipcode)
