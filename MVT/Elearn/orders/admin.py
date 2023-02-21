from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ('product',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'created', 'updated', 'has_paid')
    list_filter = ('has_paid', 'created', 'updated')
    search_fields = ('first_name', 'last_name', 'city')
    inlines = (OrderItemInline,)
