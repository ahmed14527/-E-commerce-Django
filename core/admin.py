from django.contrib import admin
from .models import Item, OrderItem, Order, Address, Payment, Coupon, Refund

admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Address)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)