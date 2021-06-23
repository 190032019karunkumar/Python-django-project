from django.contrib import admin

# Register your models here.

from .models import Bid,Product,Daily,All,Offer

admin.site.register(Bid),
admin.site.register(Product),
admin.site.register(Daily),
admin.site.register(All),
admin.site.register(Offer),