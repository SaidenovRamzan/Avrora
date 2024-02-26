from django.test import TestCase, Client
from django.urls import reverse
from documents.models import Document
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile


class DocumentListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_superuser(
            email="test@example.com", password="password"
        )
        self.client.login(email="test@example.com", password="password")
        self.document_list_url = reverse("document_list")

    def test_document_list_view_with_login(self):
        response = self.client.get(self.document_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Document List")
        self.assertQuerysetEqual(
            response.context["documents"],
            Document.objects.filter(user=self.user),
            transform=lambda x: x,
        )

    def test_document_list_view_without_login(self):
        self.client.logout()
        response = self.client.get(self.document_list_url)
        self.assertEqual(response.status_code, 302)


class DocumentDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            email="test@example.com", password="password"
        )
        self.superuser = get_user_model().objects.create_superuser(
            email="admin@example.com", password="adminpassword"
        )
        # Создаем текстовый файл для тестирования
        file_content = b"This is a test file content"
        self.uploaded_file = SimpleUploadedFile("test_file.txt", file_content)
        self.document = Document.objects.create(
            user=self.user,
            name="Test Document",
            description="Test Description",
            file=self.uploaded_file,
        )

    def test_document_detail_view_with_author(self):
        self.client.login(email="test@example.com", password="password")
        response = self.client.get(
            reverse("document_detail", kwargs={"pk": self.document.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "document_detail.html")

    def test_document_detail_view_with_superuser(self):
        self.client.login(email="admin@example.com", password="adminpassword")
        response = self.client.get(
            reverse("document_detail", kwargs={"pk": self.document.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "document_detail.html")

    def test_document_detail_view_with_unauthorized_user(self):
        response = self.client.get(
            reverse("document_detail", kwargs={"pk": self.document.pk})
        )
        self.assertEqual(response.status_code, 403)


class DocumentCreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            email="test@example.com", password="password"
        )
        self.client.login(email="test@example.com", password="password")
        self.document_create_url = reverse("document_create")

    def test_document_create_view(self):
        file_content = b"This is a test file content"
        self.uploaded_file = SimpleUploadedFile("test_file.txt", file_content)
        response = self.client.post(
            self.document_create_url,
            {
                "name": "New Document",
                "description": "Test Description",
                "file": self.uploaded_file,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("document_list"))
        self.assertTrue(Document.objects.filter(name="New Document").exists())


class DocumentUpdateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            email="test@example.com", password="password"
        )
        self.client.login(email="test@example.com", password="password")

        # Создаем текстовый файл для тестирования
        file_content = b"This is a test file content"
        self.uploaded_file = SimpleUploadedFile("test_file.txt", file_content)
        self.document = Document.objects.create(
            user=self.user,
            name="Test Document",
            description="Test Description",
            file=self.uploaded_file,
        )
        self.document_update_url = reverse(
            "document_update", kwargs={"pk": self.document.pk}
        )

    def test_document_update_view(self):
        # Создаем текстовый файл для тестирования
        file_content = b"This is a test file content"
        self.uploaded_file = SimpleUploadedFile("test_file.txt", file_content)
        response = self.client.post(
            self.document_update_url,
            {
                "name": "Updated Document",
                "description": "Updated Description",
                "file": self.uploaded_file,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("document_list"))
        self.document.refresh_from_db()
        self.assertEqual(self.document.name, "Updated Document")


class DocumentDeleteViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            email="test@example.com", password="password"
        )
        self.client.login(email="test@example.com", password="password")

        # Создаем текстовый файл для тестирования
        file_content = b"This is a test file content"
        self.uploaded_file = SimpleUploadedFile("test_file.txt", file_content)
        self.document = Document.objects.create(
            user=self.user,
            name="Test Document",
            description="Test Description",
            file=self.uploaded_file,
        )
        self.document_delete_url = reverse(
            "document_delete", kwargs={"pk": self.document.pk}
        )

    def test_document_delete_view(self):
        response = self.client.post(self.document_delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("document_list"))
        self.assertFalse(Document.objects.filter(name="Test Document").exists())
