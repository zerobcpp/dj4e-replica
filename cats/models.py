from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.


class Breed(models.Model):
    name = models.CharField(max_length=200, validators=[MinLengthValidator(2, ">= 2 characters for breedtype")])
    
    def __str__(self):
        return self.name
    
class Cats(models.Model):
    nickname = models.CharField(max_length=100,
                            validators=[MinLengthValidator(2, "Name must be >= 2 characters")], verbose_name='name')
    weight = models.PositiveIntegerField()
    foods = models.CharField(max_length=300)
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, null = False)
    
    def __str__(self):
        return self.nickname