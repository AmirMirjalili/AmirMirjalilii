from decimal import Decimal
from django.db import models
from django.conf import settings
from product.models import Product

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id} for {self.user}"

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())

    def get_discounted_price(self):
        total_price = self.get_total_price()
        return total_price - self.get_total_discount()

    def get_total_discount(self):
        return sum(item.get_discount_amount() for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    def get_total_price(self):
        return int(self.product.price) * self.quantity

    def get_discount_amount(self):
        if self.product.discount_percentage > 0:
            discount = self.product.price * (self.product.discount_percentage / Decimal(100))
            return discount * self.quantity
        return Decimal(0)

    def get_discounted_price(self):
        if self.product.discount_percentage > 0:
            discount = self.product.price * (self.product.discount_percentage / Decimal(100))
            return (self.product.price - discount) * self.quantity
        return self.get_total_price()

