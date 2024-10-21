from django.db import models
from api.category.models import Category
from django.core.validators import MinLengthValidator, MinValueValidator
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=256, 
                            validators=[MinLengthValidator(5, "Product name must be bigger than 5 characters")])
    description = models.CharField(max_length = 500)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    stock = models.IntegerField(validators=[MinValueValidator(0, "It must be greater than 0 stock")])
    active = models.BooleanField(default=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
    def __str__(self):
        return self.name 