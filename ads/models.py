from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings
    
# Create your models here.

class Ad(models.Model):
    title = models.CharField(max_length=200, 
                             validators=[MinLengthValidator(2, 'Must be greater than 2 characters')])
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    picture = models.BinaryField(null=True, editable=True)
    content_type = models.CharField(max_length=256, null=True, help_text='The MIMEType of the file')
    
    def __str__(self):
        return self.title


