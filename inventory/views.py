from django.shortcuts import render
import requests

def inventory_list(request):
    response = requests.get('http://localhost:8000/api/inventory/')
    inventories = response.json() if response.status_code == 200 else []

    return render(request, 'inventory/inventory_list.html', {'inventories': inventories})
