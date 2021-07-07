from django.contrib import admin

# Register your models here.
from .models import Customer, Product, order, Tag

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(order)
