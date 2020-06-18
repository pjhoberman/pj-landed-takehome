from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient
from rest_framework import status

from .models import Agent, Region


class TestAPI(TestCase):
    fixtures = ['agents.json', ]

    def test_all_agents_endpoint(self):
        client = APIClient()

        # no filter
        response = client.get('/agent/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        agents = response.json()
        self.assertEqual(len(agents), 10)

        # filter first name
        response = client.get('/agent/', data={'first_name': 'rob'})
        agents = response.json()
        self.assertEqual(len(agents), 2)

        rob = Agent.objects.get(pk=12)
        brent = Agent.objects.get(pk=21)
        self.assertIn(rob.pk, [agent['id'] for agent in agents])
        self.assertNotIn(brent.pk, [agent['id'] for agent in agents])

        # filter first_time_agent bool
        response = client.get('/agent/', data={'first_time_agent': 'true'})
        agents = response.json()
        self.assertTrue(all([agent['first_time_agent'] for agent in agents]))

        response = client.get('/agent/', data={'first_time_agent': 'false'})
        agents = response.json()
        self.assertFalse(any([agent['first_time_agent'] for agent in agents]))

        # test multiple persona
        response = client.get('/agent/?persona=mild&persona=prof')
        agents = response.json()
        personas = set([agent['persona'] for agent in agents])
        self.assertEqual(personas, {"Mild", "Professorial"})

    def test_agent_filter(self):
        client = APIClient()

        # test region
        response = client.get('/agent/region/haw')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        agents = response.json()
        self.assertTrue(all([True if agent['region'] == "Hawaii" else False for agent in agents]))

        # test bad filter
        response = client.get('/agent/location/home')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_agent_detail(self):
        client = APIClient()

        # test good call
        response = client.get('/agent/12')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        agent = response.json()
        self.assertEqual(agent['id'], 12)
        self.assertEqual(agent['last_name'], "Whistler")

        # test bad call
        response = client.get('agent/243930')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)






