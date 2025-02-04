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
        serializer = InventorySerializer(inventories, many=True)
        return Response(serializer.data)

