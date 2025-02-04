from django.db import models
from django.core.exceptions import ValidationError

class Supplier(models.Model):
    name = models.CharField(max_length = 50, unique = True)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)     

    def __str__(self):
        return self.name

def validate_max_length(value):
    max_length = 1000
    if len(value) > max_length:
        raise ValidationError(f"Text exceeds the maximum length of {max_length} characters.")

class Inventory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100, null=True)
    note = models.TextField(validators=[validate_max_length])
    stock = models.PositiveIntegerField(null=False, default=0)
    availability = models.BooleanField(null=False, default=False)
    supplier = models.ForeignKey(Supplier, related_name="inventories", on_delete=models.SET_NULL, null = True)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name