from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
from ..models import Inventory, Supplier

class InventoryViewsTestCase(TestCase):

    def setUp(self):
        """Set up test inventory data"""
        self.supplier = Supplier.objects.create(name="Supplier")
        self.inventory = Inventory.objects.create(
            name="Test Item", 
            supplier=self.supplier, 
            availability=True
        )

    @patch('requests.get')
    def test_inventory_list_status(self, mock_get):
        """Test that the /inventory page returns 200 OK and expected template"""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {'name': 'Test Item', 'supplier_name': 'Supplier', 'availability': True}
        ]

        response = self.client.get(reverse('inventory_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory/inventory_list.html')

    def test_inventory_detail_status(self):
        """Test that the /inventory/<id> page returns 200 OK with correct data"""
        response = self.client.get(reverse('inventory_details', args=[self.inventory.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory/inventory_details.html')
        self.assertContains(response, "Test Item")

    def test_inventory_detail_not_found(self):
        """Test that accessing a non-existent inventory returns 404"""
        response = self.client.get(reverse('inventory_details', args=[999]))
        self.assertEqual(response.status_code, 404)

    @patch('requests.get')
    def test_api_inventory_status(self, mock_get):
        """Test that the /api/inventory page returns 200 OK"""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = []

        response = self.client.get('/api/inventory/')  
        self.assertEqual(response.status_code, 200)
