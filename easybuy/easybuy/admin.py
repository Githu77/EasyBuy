from django.contrib import admin

# Register your models here.
from .models import UserProfile, Category, Product, Cart, CartItem, Order, OrderItem, Review

admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)
