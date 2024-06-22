import pytest
from django.test import TestCase

from inventory.models import Item, Supplier


@pytest.mark.django_db
class TestModels(TestCase):
    def test_supplier_creation(self):
        supplier = Supplier.objects.create(
            name="Supplier 1", contact="Supplier Contact details"
        )
        assert supplier.name == "Supplier 1"
        assert supplier.contact == "Supplier Contact details"

    def test_item_creation(self):
        supplier = Supplier.objects.create(name="Supplier 2", contact="Contact details")
        item = Item.objects.create(
            name="Item 1", description="Item description", price=10.99
        )
        item.suppliers.add(supplier)

        assert item.name == "Item 1"
        assert item.description == "Item description"
        assert item.price == 10.99
        assert item.date_added is not None
        assert supplier in item.suppliers.all()

    def test_item_str_method(self):
        item = Item.objects.create(
            name="Test Item", description="Test Description", price=5.99
        )
        assert str(item) == "Test Item"

    def test_supplier_str_method(self):
        supplier = Supplier.objects.create(
            name="Test Supplier", contact="Contact details"
        )
        assert str(supplier) == "Test Supplier"
