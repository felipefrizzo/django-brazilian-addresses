from django.shortcuts import resolve_url
from rest_framework import status
from rest_framework.test import APITestCase

from addresses.models import State, City, Neighborhood, Street


class StreetViewTest(APITestCase):
    def setUp(self):
        state = State.objects.create(name='Paraná', initials='PR')
        city = City.objects.create(name='Cascavel', state=state)
        neigh = Neighborhood.objects.create(name='Santa Felicidade', city=city)
        Street.objects.create(
            name='Rua João Ribeiro Pinheiro',
            zipcode='85803260', neighborhood=neigh
        )

        self.response = self.client.get(resolve_url('street-list'))

    def test_view(self):
        """GET /street/ must return status code 200."""
        self.assertEqual(status.HTTP_200_OK, self.response.status_code)

    def test_list(self):
        """Ensure we can list all streets"""
        self.assertEqual(1, len(self.response.data))


class StreetViewGetTest(APITestCase):
    def setUp(self):
        State.objects.create(name='Paraná', initials='PR')
        self.url = resolve_url('street-detail', zipcode='85803260')

    def test_exists(self):
        self.assertFalse(Street.objects.exists())

    def test_view(self):
        response = self.client.get(self.url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertTrue(Street.objects.exists())


class StreetViewInvalidGetTest(APITestCase):
    def setUp(self):
        State.objects.create(name='Paraná', initials='PR')
        self.response = self.client.get(
            resolve_url('street-detail', zipcode='97979777')
        )

    def test_view(self):
        """Invalid GET /street/<int:zipcode> must return status code 404."""
        self.assertEqual(status.HTTP_404_NOT_FOUND, self.response.status_code)


class StreetViewInvalidPostTest(APITestCase):
    def setUp(self):
        state = State.objects.create(name='Paraná', initials='PR')
        city = City.objects.create(name='Cascavel', state=state)
        neigh = Neighborhood.objects.create(name='Santa Felicidade', city=city)

        self.response = self.client.post(
            resolve_url('street-list'),
            dict(
                name='João Ribeiro Pinheiro',
                zipcode='85803260', neighborhood=neigh.pk
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
        state = State.objects.create(name='Paraná', initials='PR')
        city = City.objects.create(name='Cascavel', state=state)
        neigh = Neighborhood.objects.create(name='Santa Felicidade', city=city)
        street = Street.objects.create(
            name='João Ribeiro Pinheiro',
            zipcode='85803260', neighborhood=neigh
        )

        self.url = resolve_url('street-detail', street.pk)

    def test_post(self):
        """Invalid post must return status code 405."""
        self.response = self.client.put(self.url, dict(name='Nova Cidade'))
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED, self.response.status_code)


class StreetViewInvalidDeleteTest(APITestCase):
    def setUp(self):
        state = State.objects.create(name='Paraná', initials='PR')
        city = City.objects.create(name='Cascavel', state=state)
        neigh = Neighborhood.objects.create(name='Santa Felicidade', city=city)
        street = Street.objects.create(
            name='João Ribeiro Pinheiro',
            zipcode='85803260', neighborhood=neigh
        )

        self.url = resolve_url('street-detail', street.pk)

    def test_post(self):
        """Invalid post must return status code 405."""
        self.response = self.client.delete(self.url)
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED, self.response.status_code)
