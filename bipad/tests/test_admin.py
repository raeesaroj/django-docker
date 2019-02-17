from django.test import TestCase


class AdminTest(TestCase):
    def test_running(self):
        resp = self.client.get('/admin/login/')
        self.assertEqual(resp.status_code, 200)
