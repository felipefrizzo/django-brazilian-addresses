from django.shortcuts import resolve_url
from rest_framework import status
from rest_framework.test import APITestCase

from django_brazilian_addresses.addresses.models import StreetType


class StreetTypeViewTest(APITestCase):
    def setUp(self):
        StreetType.objects.create(name='Rua')
        self.response = self.client.get(resolve_url('streettype-list'))

    def test_view(self):
        """GET /street_type/ must return status code 200."""
        self.assertEqual(status.HTTP_200_OK, self.response.status_code)

    def test_list(self):
        """Ensure we can list all street types"""
        self.assertEqual(1, len(self.response.data))


class StreetTypeViewInvalidPostTest(APITestCase):
    def setUp(self):
        self.response = self.client.post(
            resolve_url('streettype-list'), dict(name='Rua'))

    def test_post(self):
        """Invalid post must return status code 405."""
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED, self.response.status_code)

    def test_dont_save(self):
        """Ensure we can't insert a new street type."""
        self.assertFalse(StreetType.objects.exists())


class StreetTypeViewInvalidUpdateTest(APITestCase):
    def setUp(self):
        street_type = StreetType.objects.create(name='Rua')
        self.url = resolve_url('streettype-detail', street_type.pk)

    def test_post(self):
        """Invalid post must return status code 405."""
        self.response = self.client.put(self.url, dict(name='Avenida'))
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED, self.response.status_code)


class StreetTypeViewInvalidDeleteTest(APITestCase):
    def setUp(self):
        street_type = StreetType.objects.create(name='Rua')
        self.url = resolve_url('streettype-detail', street_type.pk)

    def test_post(self):
        """Invalid post must return status code 405."""
        self.response = self.client.delete(self.url)
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED, self.response.status_code)
