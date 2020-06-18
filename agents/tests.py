from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient
from rest_framework import status

from .models import Agent


class TestAPI(TestCase):
    fixtures = ['agents.json', ]

    def test_all_agents_endpoint(self):
        client = APIClient()

        # no filter
        request = client.get('/agent/')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        agents = request.json()
        self.assertEqual(len(agents), 10)

        # filter first name
        request = client.get('/agent/', data={'first_name': 'rob'})
        agents = request.json()
        self.assertEqual(len(agents), 2)

        rob = Agent.objects.get(pk=12)
        brent = Agent.objects.get(pk=21)
        self.assertIn(rob.pk, [agent['id'] for agent in agents])
        self.assertNotIn(brent.pk, [agent['id'] for agent in agents])

        # filter first_time_agent bool
        request = client.get('/agent/', data={'first_time_agent': 'true'})
        agents = request.json()
        self.assertTrue(all([agent['first_time_agent'] for agent in agents]))

        request = client.get('/agent/', data={'first_time_agent': 'false'})
        agents = request.json()
        self.assertFalse(any([agent['first_time_agent'] for agent in agents]))








