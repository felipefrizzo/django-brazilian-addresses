from django.shortcuts import resolve_url
from rest_framework import status
from rest_framework.test import APITestCase

from django_brazilian_addresses.addresses.models import Country


class CountryViewTest(APITestCase):
    def setUp(self):
        Country.objects.create(name='Brasil')
        self.response = self.client.get(resolve_url('country-list'))

    def test_view(self):
        """GET /country/ must return status code 200."""
        self.assertEqual(status.HTTP_200_OK, self.response.status_code)

    def test_list(self):
        """Ensure we can list all countries"""
        self.assertEqual(1, len(self.response.data))


class CountryViewInvalidPostTest(APITestCase):
    def setUp(self):
        self.response = self.client.post(
            resolve_url('country-list'), dict(name='Brasil'))

    def test_post(self):
        """Invalid post must return status code 405."""
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED, self.response.status_code)

    def test_dont_save(self):
        """Ensure we can't insert a new country."""
        self.assertFalse(Country.objects.exists())


class CountryViewInvalidUpdateTest(APITestCase):
    def setUp(self):
        country = Country.objects.create(name='Brasil')
        self.url = resolve_url('country-detail', country.pk)

    def test_post(self):
        """Invalid post must return status code 405."""
        self.response = self.client.put(self.url, dict(name='Panamá'))
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED, self.response.status_code)


class CountryViewInvalidDeleteTest(APITestCase):
    def setUp(self):
        country = Country.objects.create(name='Brasil')
        self.url = resolve_url('country-detail', country.pk)

    def test_post(self):
        """Invalid post must return status code 405."""
        self.response = self.client.delete(self.url)
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED, self.response.status_code)
