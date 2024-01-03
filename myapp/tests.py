from django.test import TestCase

# Create your tests here.
# myapp/tests.py

from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Invoice, InvoiceDetail

class InvoiceAPITestCase(APITestCase):
    def setUp(self):
        self.invoice = Invoice.objects.create(date='2024-01-01', customer_name='Test Customer')
        self.invoice_detail = InvoiceDetail.objects.create(
            invoice=self.invoice,
            description='Test Description',
            quantity=2,
            unit_price=10.0,
            price=20.0
        )

    def test_invoice_list(self):
        url = reverse('invoice-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # Add more test cases for other HTTP methods and endpoints

    