from django.shortcuts import render, get_object_or_404
import requests
from requests.exceptions import RequestException
from .models import Inventory

def inventory_list(request):
    name = request.GET.get('name', '')
    supplier_name = request.GET.get('supplier_name', '')
    availability = request.GET.get('availability', '')

    api_url = 'http://localhost:8000/api/inventory/'
    params = {}

    if name:
        params['name'] = name
    if availability:
        params['availability'] = availability.lower() == 'true'
    if supplier_name:
        params['supplier_name'] = supplier_name

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status() 
        inventories = response.json() if response.status_code == 200 else []
    except RequestException as e:
        inventories = []
        print(f"Error fetching data from API: {e}")

    return render(request, 'inventory/inventory_list.html', {'inventories': inventories})

def inventory_details(request,  id):
    inventory_details = get_object_or_404(Inventory, id=id)
    return render(request, 'inventory/inventory_details.html', {'inventory': inventory_details})
