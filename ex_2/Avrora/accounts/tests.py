from django.test import TestCase, Client
from django.urls import reverse


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse("login")
        self.logout_url = reverse("logout")
        self.user_create_url = reverse("user_create")
        self.document_list_url = reverse("document_list")

    def test_custom_login_view(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")

        response = self.client.post(
            self.login_url, {"email": "test@example.com", "password": "password"}
        )
        self.assertEqual(response.status_code, 200)

    def test_custom_logout_view(self):
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)

    def test_user_create_view(self):
        response = self.client.get(self.user_create_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user_create.html")

        response = self.client.post(
            self.user_create_url,
            {
                "username": "testuser",
                "email": "test@example.com",
                "password1": "password",
                "password2": "password",
            },
        )
        self.assertEqual(response.status_code, 200)
