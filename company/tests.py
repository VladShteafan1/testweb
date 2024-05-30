from django.test import TestCase, Client
from django.urls import reverse
from .models import Service
from .forms import ServiceForm

class CompanyTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.service = Service.objects.create(name="Test Service", description="Test Description")

    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_services_page_status_code(self):
        response = self.client.get(reverse('services'))
        self.assertEqual(response.status_code, 200)

    def test_services_page_contains_service(self):
        response = self.client.get(reverse('services'))
        self.assertContains(response, "Test Service")

    def test_contact_page_status_code(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_add_service(self):
        response = self.client.post(reverse('services'), {
            'name': 'New Service',
            'description': 'New Description'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after post
        self.assertEqual(Service.objects.count(), 2)
        self.assertEqual(Service.objects.last().name, 'New Service')

class CompanyFormTests(TestCase):
    def test_service_form_valid(self):
        form = ServiceForm(data={
            'name': 'Service Name',
            'description': 'Service Description'
        })
        self.assertTrue(form.is_valid())

    def test_service_form_invalid(self):
        form = ServiceForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)
