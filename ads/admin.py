from django.contrib import admin
from ads.models import Ad
# Register your models here.



class Ads_Admin(admin.ModelAdmin):
    exclude = ('picture', 'content_type')


# Register the admin class with the associated model
admin.site.register(Ad, Ads_Admin)
