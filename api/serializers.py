from rest_framework import serializers
from inventory.models import Inventory, Supplier

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ["name"]

class InventorySerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(read_only=True)

    class Meta:
        model = Inventory
        fields = "__all__"
        read_only_fields = ["id", "added_at", "updated_at"]

