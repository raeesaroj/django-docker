from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class EventTests(APITestCase):
    def test_list(self):
        """
        Ensure we can list events.
        """
        url = reverse(
            'event-list',
            kwargs={
                'version': 'v1'
            }
        )
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
