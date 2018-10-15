from django.shortcuts import resolve_url
from rest_framework import status
from rest_framework.test import APITestCase

from django_brazilian_addresses.addresses.models import State


class StateViewTest(APITestCase):
    def setUp(self):
        State.objects.create(name='Paraná', initials='PR')
        self.response = self.client.get(resolve_url('state-list'))

    def test_view(self):
        """GET /state/ must return status code 200."""
        self.assertEqual(status.HTTP_200_OK, self.response.status_code)

    def test_list(self):
        """Ensure we can list all states"""
        self.assertEqual(1, len(self.response.data))


class StateViewInvalidPostTest(APITestCase):
    def setUp(self):
        self.response = self.client.post(
            resolve_url('state-list'),
            dict(name='Paraná', initials='PR')
        )

    def test_post(self):
        """Invalid post must return status code 405."""
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED, self.response.status_code)

    def test_dont_save(self):
        """Ensure we can't insert a new state."""
        self.assertFalse(State.objects.exists())


class StateViewInvalidUpdateTest(APITestCase):
    def setUp(self):
        state = State.objects.create(name='Paraná', initials='PR')
        self.url = resolve_url('state-detail', state.pk)

    def test_post(self):
        """Invalid post must return status code 405."""
        self.response = self.client.put(self.url, dict(name='São Paulo'))
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED, self.response.status_code)


class StateViewInvalidDeleteTest(APITestCase):
    def setUp(self):
        state = State.objects.create(name='Paraná', initials='PR')
        self.url = resolve_url('state-detail', state.pk)

    def test_post(self):
        """Invalid post must return status code 405."""
        self.response = self.client.delete(self.url)
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED, self.response.status_code)
