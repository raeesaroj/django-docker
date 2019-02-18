import json
from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User


class LoginTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='admin',
            first_name='First',
            last_name='Last',
            password='admin123',
            email='test@test.com',
            is_superuser=False,
            is_staff=False,
        )

    def authenticate(self, username="", password=""):
        url = reverse(
            "token_obtain_pair",
            kwargs={
                "version": "v1"
            }
        )

        return self.client.post(
            url,
            data=json.dumps({
                "username": username,
                "password": password
            }),
            content_type="application/json"
        )

    def test_valid_user(self):
        response = self.authenticate("admin", "admin123")
        self.assertEqual(response.status_code, 200)

    def test_invalid_user(self):
        response = self.authenticate("admin", "wrongpassword")
        self.assertEqual(response.status_code, 400)
