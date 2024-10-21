from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100,
                            validators=[MinLengthValidator(2, 'Category name invalid, must be more than 2 words')]
                            )
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name