import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from inventory.models import Item, Supplier


@pytest.mark.django_db
class TestItemViewSet:
    def setup_method(self):
        self.client = APIClient()
        self.supplier = Supplier.objects.create(name="Test Supplier", contact="1234")
        self.item = Item.objects.create(
            name="Test Item", description="This is a test item", price=10.00
        )
        self.item.suppliers.add(self.supplier)
        self.item_url = reverse("item-detail", args=[self.item.id])
        self.list_url = reverse("item-list")

    def test_list_items(self):
        response = self.client.get(self.list_url)
        assert response.status_code == 200
        assert response.data["status"] == "success"
        assert response.data["response_code"] == "00"
        assert len(response.data["response"]) == 1

    def test_retrieve_item(self):
        response = self.client.get(self.item_url)
        assert response.status_code == 200
        assert response.data["status"] == "success"
        assert response.data["response_code"] == "00"
        assert response.data["response"]["name"] == self.item.name

    def test_retrieve_non_existent_item(self):
        url = reverse("item-detail", args=[9999])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data["status"] == "error"
        assert response.data["response_code"] == "99"

    def test_create_item(self):
        data = {
            "name": "New Item",
            "description": "This is a new item",
            "price": 15.00,
            "suppliers": [self.supplier.id],
        }
        response = self.client.post(self.list_url, data, format="json")
        assert response.status_code == 201
        assert response.data["status"] == "success"
        assert response.data["response_code"] == "00"
        assert response.data["response"]["name"] == "New Item"

    def test_create_invalid_item(self):
        data = {"name": ""}
        response = self.client.post(self.list_url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["status"] == "error"
        assert response.data["response_code"] == "99"

    def test_update_item(self):
        data = {
            "name": "Updated Item",
            "description": "This is an updated item",
            "price": 20.00,
            "suppliers": [self.supplier.id],
        }
        response = self.client.put(self.item_url, data, format="json")
        assert response.status_code == 200
        assert response.data["status"] == "success"
        assert response.data["response_code"] == "00"
        assert response.data["response"]["name"] == "Updated Item"

    def test_update_non_existent_item(self):
        url = reverse("item-detail", args=[9999])
        data = {"name": "Updated Item"}
        response = self.client.put(url, data, format="json")
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data["status"] == "error"
        assert response.data["response_code"] == "99"

    def test_destroy_item(self):
        response = self.client.delete(self.item_url)
        assert response.status_code == 204
        assert response.data["status"] == "success"
        assert response.data["response_code"] == "00"

    def test_delete_non_existent_item(self):
        url = reverse("item-detail", args=[9999])
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data["status"] == "error"
        assert response.data["response_code"] == "99"


@pytest.mark.django_db
class TestSupplierViewSet:
    def setup_method(self):
        self.client = APIClient()
        self.supplier = Supplier.objects.create(name="Test Supplier", contact="1234")
        self.supplier_url = reverse("supplier-detail", args=[self.supplier.id])
        self.list_url = reverse("supplier-list")

    def test_list_suppliers(self):
        response = self.client.get(self.list_url)
        assert response.status_code == 200
        assert response.data["status"] == "success"
        assert response.data["response_code"] == "00"
        assert len(response.data["response"]) == 1

    def test_retrieve_supplier(self):
        response = self.client.get(self.supplier_url)
        assert response.status_code == 200
        assert response.data["status"] == "success"
        assert response.data["response_code"] == "00"
        assert response.data["response"]["name"] == self.supplier.name

    def test_retrieve_non_existent_supplier(self):
        url = reverse("supplier-detail", args=[9999])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data["status"] == "error"
        assert response.data["response_code"] == "99"

    def test_create_supplier(self):
        data = {"name": "New Supplier", "contact": "5678"}
        response = self.client.post(self.list_url, data, format="json")
        assert response.status_code == 201
        assert response.data["status"] == "success"
        assert response.data["response_code"] == "00"
        assert response.data["response"]["name"] == "New Supplier"

    def test_create_invalid_supplier(self):
        data = {"name": ""}
        response = self.client.post(self.list_url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["status"] == "error"
        assert response.data["response_code"] == "99"

    def test_update_supplier(self):
        data = {"name": "Updated Supplier", "contact": "5678"}
        response = self.client.put(self.supplier_url, data, format="json")
        assert response.status_code == 200
        assert response.data["status"] == "success"
        assert response.data["response_code"] == "00"
        assert response.data["response"]["name"] == "Updated Supplier"

    def test_update_non_existent_supplier(self):
        url = reverse("supplier-detail", args=[9999])
        data = {"name": "Updated supplier"}
        response = self.client.put(url, data)
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data["status"] == "error"
        assert response.data["response_code"] == "99"

    def test_destroy_supplier(self):
        response = self.client.delete(self.supplier_url)
        assert response.status_code == 204
        response = self.client.get(self.supplier_url)
        assert response.status_code == 404

    def test_delete_non_existent_supplier(self):
        url = reverse("supplier-detail", args=[9999])
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data["status"] == "error"
        assert response.data["response_code"] == "99"


@pytest.mark.django_db
class TestSuppliersForItemApiView:
    def setup_method(self):
        self.client = APIClient()

        # Let's create Suppliers
        self.supplier1 = Supplier.objects.create(name="Supplier 1", contact="Contact 1")
        self.supplier2 = Supplier.objects.create(name="Supplier 2", contact="Contact 2")

        # Then we create Item and associate with suppliers
        self.item = Item.objects.create(
            name="Item 1", description="Description 1", price=10.00
        )
        self.item.suppliers.add(self.supplier1, self.supplier2)

        self.item_url = reverse("items_supplier", args=[self.item.id])

    def test_get_suppliers_for_item(self):
        response = self.client.get(self.item_url)
        assert response.status_code == 200
        assert response.data["status"] == "success"
        assert response.data["response_code"] == "00"
        assert len(response.data["response"]) == 2
        supplier_names = [supplier["name"] for supplier in response.data["response"]]
        assert "Supplier 1" in supplier_names
        assert "Supplier 2" in supplier_names


@pytest.mark.django_db
class TestItemForSupplierApiView:
    def setup_method(self):
        self.client = APIClient()

        # Create Suppliers
        self.supplier = Supplier.objects.create(name="Supplier 1", contact="Contact 1")

        # Create Items and associate with supplier
        self.item1 = Item.objects.create(
            name="Item 1", description="Description 1", price=10.00
        )
        self.item2 = Item.objects.create(
            name="Item 2", description="Description 2", price=20.00
        )
        self.item1.suppliers.add(self.supplier)
        self.item2.suppliers.add(self.supplier)

        self.supplier_url = reverse("suppliers_item", args=[self.supplier.id])

    def test_get_items_for_supplier(self):
        response = self.client.get(self.supplier_url)
        assert response.status_code == 200
        assert response.data["status"] == "success"
        assert response.data["response_code"] == "00"
        assert len(response.data["response"]) == 2
        item_names = [item["name"] for item in response.data["response"]]
        assert "Item 1" in item_names
        assert "Item 2" in item_names
