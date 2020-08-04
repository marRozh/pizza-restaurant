from django.contrib import admin

from .models import Item, Size, Topping, Subtopping, Order, Confirmed, Complete

# Register your models here.
admin.site.register(Item)
admin.site.register(Size)
admin.site.register(Topping)
admin.site.register(Subtopping)
admin.site.register(Order)
admin.site.register(Confirmed)
admin.site.register(Complete)