from django.contrib import admin
from .models import Product, Order


# Register your models here.

admin.site.site_header = "E-Scooters & E-Bikes Shopping"
admin.site.index_title = "Manage E-Scooters & E-Bikes Shopping Site"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'discount_price', 'category', 'description', )


class OrderAdmin(admin.ModelAdmin):
    list_display = ('items', 'name', 'email', 'address', 'city', 'zipcode', 'region', 'total' )


admin.site.register(Product,ProductAdmin)
admin.site.register(Order, OrderAdmin)