from django.db import models
from django.core.validators import MinLengthValidator
from api.user.models import CustomUser
from api.product.models import Product

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name=(""), on_delete=models.CASCADE, null=True, blank=True)
    
    product_names = models.CharField(max_length=500, validators=[MinLengthValidator(2, "name must be longer")])
    transaction_id = models.CharField(max_length=150, default='0')
    total_products = models.CharField(max_length=150, default='0')
    total_amount = models.CharField(max_length=150, default='0')
    
    created_at = models.DateField(auto_now_add=True)
    updated_at =models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.product_names}"