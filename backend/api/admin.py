from django.contrib import admin
from .models import User,Category,Product,Order,OrderItem,Payment

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)