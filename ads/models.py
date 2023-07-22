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
    comments = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Comment',  related_name=('comments_owned'))
    favorites = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Fav', related_name='Favorite_ads')
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField(validators=[MinLengthValidator(3, 'Comments must be more than 3 characters')])
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        if len(self.text) < 15: 
            return self.text
        return self.text[:11] + ' ...'

class Fav(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('ad', 'user')

    def __str__(self):
        return f'{self.user.username} likes {self.ad.title[:10]}'
