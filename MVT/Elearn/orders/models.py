from django.db import models
from shop.models import Product

# Create your models here.
class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.TextField()
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=False)
    has_paid = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('-created',)
        
    def __str__(self):
        return f'Order {self.id}'
    
    def get_total_cost(self):
        return sum(item.get_cost for item in self.items.all())
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return str(self.id)
    
    def get_cost(self):
        return self.quantity * self.price
