from datetime import datetime

from django.shortcuts import resolve_url
from django.test import TestCase

from addresses.models import State


class StateModelTest(TestCase):
    def setUp(self):
        self.state = State.objects.create(name='Paraná', initials='PR')

    def test_create(self):
        self.assertTrue(State.objects.exists())

    def test_str(self):
        self.assertEqual('Paraná', str(self.state))

    def test_get_state_initials(self):
        self.assertEqual('PR', self.state.initials)

    def test_absolute_url(self):
        url = resolve_url('state-detail', self.state.pk)
        self.assertEqual(url, self.state.get_absolute_url())

    def test_create_date(self):
        """State must have an auto created_at attrs."""
        self.assertIsInstance(self.state.created_at, datetime)

    def test_update_date(self):
        """State must have an auto updated_at attrs."""
        self.assertIsInstance(self.state.updated_at, datetime)
