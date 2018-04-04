from django.shortcuts import resolve_url
from rest_framework import status
from rest_framework.test import APITestCase

from django_brazilian_addresses.addresses.models import Country, State, City, \
    Neighborhood, StreetType, Street


class StreetViewTest(APITestCase):
    def setUp(self):
        country = Country.objects.create(name='Brasil')
        state = State.objects.create(name='Paraná', country=country)
        city = City.objects.create(name='Cascavel', state=state)
        neigh = Neighborhood.objects.create(name='Santa Felicidade', city=city)
        street_type = StreetType.objects.create(name='Rua')
        Street.objects.create(
            name='João Ribeiro Pinheiro', zipcode='85803260',
            neighborhood=neigh, street_type=street_type
        )

        self.response = self.client.get(resolve_url('street-list'))

    def test_view(self):
        """GET /street/ must return status code 200."""
        self.assertEqual(status.HTTP_200_OK, self.response.status_code)

    def test_list(self):
        """Ensure we can list all streets"""
        self.assertEqual(1, len(self.response.data))


class StreetViewInvalidPostTest(APITestCase):
    def setUp(self):
        country = Country.objects.create(name='Brasil')
        state = State.objects.create(name='Paraná', country=country)
        city = City.objects.create(name='Cascavel', state=state)
        neigh = Neighborhood.objects.create(name='Santa Felicidade', city=city)
        street_type = StreetType.objects.create(name='Rua')

        self.response = self.client.post(
            resolve_url('street-list'),
            dict(
                name='João Ribeiro Pinheiro', zipcode='85803260',
                neighborhood=neigh.pk, street_type=street_type.pk
            )
        )

    def test_post(self):
        """Invalid post must return status code 405."""
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED, self.response.status_code)

    def test_dont_save(self):
        """Ensure we can't insert a new street."""
        self.assertFalse(Street.objects.exists())


class StreetViewInvalidUpdateTest(APITestCase):
    def setUp(self):
        country = Country.objects.create(name='Brasil')
        state = State.objects.create(name='Paraná', country=country)
        city = City.objects.create(name='Cascavel', state=state)
        neigh = Neighborhood.objects.create(name='Santa Felicidade', city=city)
        street_type = StreetType.objects.create(name='Rua')
        street = Street.objects.create(
            name='João Ribeiro Pinheiro', zipcode='85803260',
            neighborhood=neigh, street_type=street_type
        )

        self.url = resolve_url('street-detail', street.pk)

    def test_post(self):
        """Invalid post must return status code 405."""
        self.response = self.client.put(self.url, dict(name='Nova Cidade'))
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED, self.response.status_code)


class StreetViewInvalidDeleteTest(APITestCase):
    def setUp(self):
        country = Country.objects.create(name='Brasil')
        state = State.objects.create(name='Paraná', country=country)
        city = City.objects.create(name='Cascavel', state=state)
        neigh = Neighborhood.objects.create(name='Santa Felicidade', city=city)
        street_type = StreetType.objects.create(name='Rua')
        street = Street.objects.create(
            name='João Ribeiro Pinheiro', zipcode='85803260',
            neighborhood=neigh, street_type=street_type
        )

        self.url = resolve_url('street-detail', street.pk)

    def test_post(self):
        """Invalid post must return status code 405."""
        self.response = self.client.delete(self.url)
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED, self.response.status_code)
