from django.shortcuts import resolve_url
from rest_framework import status
from rest_framework.test import APITestCase

from django_brazilian_addresses.addresses.models import State, City, \
    Neighborhood


class NeighborhoodViewTest(APITestCase):
    def setUp(self):
        state = State.objects.create(name='Paraná', initials='PR')
        city = City.objects.create(name='Cascavel', state=state)
        Neighborhood.objects.create(name='Santa Felicidade', city=city)

        self.response = self.client.get(resolve_url('neighborhood-list'))

    def test_view(self):
        """GET /neighborhood/ must return status code 200."""
        self.assertEqual(status.HTTP_200_OK, self.response.status_code)

    def test_list(self):
        """Ensure we can list all neighborhoods"""
        self.assertEqual(1, len(self.response.data))


class NeighborhoodViewInvalidPostTest(APITestCase):
    def setUp(self):
        state = State.objects.create(name='Paraná', initials='PR')
        city = City.objects.create(name='Cascavel', state=state)

        self.response = self.client.post(
            resolve_url('neighborhood-list'),
            dict(name='Santa Felicidade', city=city.pk)
        )

    def test_post(self):
        """Invalid post must return status code 405."""
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED, self.response.status_code)

    def test_dont_save(self):
        """Ensure we can't insert a new neighborhood."""
        self.assertFalse(Neighborhood.objects.exists())


class NeighborhoodViewInvalidUpdateTest(APITestCase):
    def setUp(self):
        state = State.objects.create(name='Paraná', initials='PR')
        city = City.objects.create(name='Cascavel', state=state)
        neigh = Neighborhood.objects.create(name='Santa Felicidade', city=city)

        self.url = resolve_url('neighborhood-detail', neigh.pk)

    def test_post(self):
        """Invalid post must return status code 405."""
        self.response = self.client.put(self.url, dict(name='Nova Cidade'))
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED, self.response.status_code)


class NeighborhoodViewInvalidDeleteTest(APITestCase):
    def setUp(self):
        state = State.objects.create(name='Paraná', initials='PR')
        city = City.objects.create(name='Cascavel', state=state)
        neigh = Neighborhood.objects.create(name='Santa Felicidade', city=city)

        self.url = resolve_url('neighborhood-detail', neigh.pk)

    def test_post(self):
        """Invalid post must return status code 405."""
        self.response = self.client.delete(self.url)
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED, self.response.status_code)
