from django.shortcuts import render, get_object_or_404
import requests
from .models import Inventory

def inventory_list(request):
    response = requests.get('http://localhost:8000/api/inventory/')
    inventories = response.json() if response.status_code == 200 else []

    return render(request, 'inventory/inventory_list.html', {'inventories': inventories})

def inventory_details(request,  id):
    inventory_details = get_object_or_404(Inventory, id=id)
    return render(request, 'inventory/inventory_details.html', {'inventory': inventory_details})
