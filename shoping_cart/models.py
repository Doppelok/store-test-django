from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

from multi_store.models import Products, UserShoppingCart


# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)


class CartItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1)])
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def increment_item(self):
        self.quantity += 1
        return self

    def decrement_item(self):
        self.quantity -= 1
        return self


class CheckoutOrder(models.Model):
    CREATED = 0
    PAID = 1
    COMPLETED = 2
    ON_WAY = 3
    DELIVERED = 4

    UKRAINE = 0
    POLAND = 1

    STATUSES = (
        (CREATED, 'CREATED'),
        (PAID, 'PAID'),
        (COMPLETED, 'COMPLETED'),
        (DELIVERED, 'DELIVERED'),
    )

    COUNTRY = (
        (UKRAINE, 'UKRAINE'),
        (POLAND, 'POLAND'),
    )

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    mobile_no = models.CharField(max_length=13)
    address = models.CharField(max_length=256)
    country = models.SmallIntegerField(default=UKRAINE, choices=COUNTRY)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    zip_code = models.PositiveSmallIntegerField()

    status = models.SmallIntegerField(default=CREATED, choices=STATUSES)
    initiator = models.ForeignKey(User, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    basket_history = models.JSONField(default=dict)

    def status_paid(self, mark):
        carts = UserShoppingCart.objects.filter(user=self.initiator)
        self.basket_history = {
            'cart': [cart.checkout_json() for cart in carts],
            'total_sum': round(carts.total_sum()),
            'total_sum_tax': round(carts.total_sum_tax()),
        }
        self.save()
        self.status = self.PAID
        carts.delete()


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)
