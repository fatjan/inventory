from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import InventorySerializer
from inventory.models import Inventory

def health_check():
    return JsonResponse({"status": "ok"})

class InventoryListView(APIView):
    def get(self, request):
        inventories = Inventory.objects.all()

        name = request.GET.get('name')
        supplier_name = request.GET.get('supplier_name')
        availability = request.GET.get('availability')

        if name:
            inventories = inventories.filter(name__icontains=name)  
        if availability is not None:
            inventories = inventories.filter(availability=availability) 
        if supplier_name:
            inventories = inventories.filter(supplier__name__icontains=supplier_name) 

        serializer = InventorySerializer(inventories, many=True)
        return Response(serializer.data)

