from django.contrib import admin
from .models import OrderDetails, OrderItem

# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ['employee', 'order_id', 'order_total', 'total_quantity', 'order_placed']
    readonly_fields = ['order_placed']
    inlines = (OrderItemInline,)

admin.site.register(OrderDetails, OrderDetailsAdmin)
#admin.site.register(OrderItem)