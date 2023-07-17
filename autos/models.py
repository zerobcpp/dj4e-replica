from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.


class Make(models.Model):
    name = models.CharField(help_text=("enter a make"), max_length=200,
                            validators=[MinLengthValidator(2, 'It must be >= 2 characters')])
    def __str__(self):
        return self.name
    
    
class Auto(models.Model):
    nickname = models.CharField(help_text='enter a nickname', max_length=200,
                                validators=[MinLengthValidator(2, 'It must be >= 2 characters')])
    mileage = models.PositiveIntegerField()
    comments = models.CharField(max_length=250)
    make = models.ForeignKey('Make', verbose_name=("fk-make"), on_delete=models.CASCADE, null=False)
    
    def __str__(self) -> str:
        return self.nickname 