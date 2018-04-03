from django.shortcuts import resolve_url
from rest_framework import status
from rest_framework.test import APITestCase

from django_brazilian_addresses.addresses.models import Country, State, City


class StateViewTest(APITestCase):
    def setUp(self):
        country = Country.objects.create(name='Brasil')
        state = State.objects.create(name='Paraná', country=country)
        City.objects.create(name='Cascavel', state=state)

        self.response = self.client.get(resolve_url('city-list'))

    def test_view(self):
        """GET /city/ must return status code 200."""
        self.assertEqual(status.HTTP_200_OK, self.response.status_code)

    def test_list(self):
        """Ensure we can list all cities"""
        self.assertEqual(1, len(self.response.data))


class StateViewInvalidPostTest(APITestCase):
    def setUp(self):
        country = Country.objects.create(name='Brasil')
        state = State.objects.create(name='Paraná', country=country)

        self.response = self.client.post(
            resolve_url('city-list'),
            dict(name='Cascavel', state=state.pk)
        )

    def test_post(self):
        """Invalid post must return status code 405."""
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED, self.response.status_code)

    def test_dont_save(self):
        """Ensure we can't insert a new city."""
        self.assertFalse(City.objects.exists())


class StateViewInvalidUpdateTest(APITestCase):
    def setUp(self):
        country = Country.objects.create(name='Brasil')
        state = State.objects.create(name='Paraná', country=country)
        city = City.objects.create(name='Cascavel', state=state)

        self.url = resolve_url('city-detail', city.pk)

    def test_post(self):
        """Invalid post must return status code 405."""
        self.response = self.client.put(self.url, dict(name='Curitiba'))
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED, self.response.status_code)


class StateViewInvalidDeleteTest(APITestCase):
    def setUp(self):
        country = Country.objects.create(name='Brasil')
        state = State.objects.create(name='Paraná', country=country)
        city = City.objects.create(name='Cascavel', state=state)

        self.url = resolve_url('city-detail', city.pk)

    def test_post(self):
        """Invalid post must return status code 405."""
        self.response = self.client.delete(self.url)
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED, self.response.status_code)
