from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

import stripe

# Create your models here.
stripe.api_key = settings.STRIPE_SECRET_KEY


class ProductsCategories(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class ProductsSubGroup(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    product_category = models.ForeignKey(ProductsCategories, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class ResolutionAttrValue(models.Model):
    name = models.CharField(max_length=64)
    value = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.value} MP'


class LensAttrValue(models.Model):
    name = models.CharField(max_length=64)
    value = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.value} mm'


class CaseAttrValue(models.Model):
    name = models.CharField(max_length=64)
    value = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.value}'


class IRAttrValue(models.Model):
    name = models.CharField(max_length=64)
    value = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.value} m'


class IPProductAttr(models.Model):
    name = models.CharField(max_length=64)
    product_group = models.ForeignKey(ProductsSubGroup, on_delete=models.CASCADE)
    resolution = models.ForeignKey(ResolutionAttrValue, on_delete=models.CASCADE, related_name='resolution')
    lens = models.ForeignKey(LensAttrValue, on_delete=models.CASCADE, related_name='lens')
    case = models.ForeignKey(CaseAttrValue, on_delete=models.CASCADE, related_name='case')
    ir = models.ForeignKey(IRAttrValue, on_delete=models.CASCADE, related_name='ir')

    def __str__(self):
        return f'{self.name}'


class Products(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    information = models.TextField()
    image = models.FileField(upload_to='products_images')
    price = models.FloatField()
    in_stock = models.PositiveIntegerField(default=0)
    product_group = models.ForeignKey(ProductsSubGroup, on_delete=models.CASCADE)
    attribute = models.ForeignKey(IPProductAttr, on_delete=models.CASCADE)

    stripe_id = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    def create_stripe_id(self):
        stripe_product = stripe.Product.create(
            name=self.name,
            default_price_data={
                'unit_amount': round(self.price * 100),
                'currency': 'usd',
            },
            expand=['default_price']
        )
        self.stripe_id = stripe_product['default_price']['id']

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.create_stripe_id()
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)


# class TypicalProductAttr(models.Model):
#     sub_group_id = models.ForeignKey(ProductsSubGroup, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200, default=None)
#
#     def __str__(self):
#         return f'{self.name}'
#
#
# class AttrValue(models.Model):
#     typical_pr_attr_id = models.ForeignKey(TypicalProductAttr, on_delete=models.CASCADE)
#     value = models.CharField(max_length=500)
#
#     def __str__(self):
#         return f'{self.value}'
#
#
# class ProductAttribute(models.Model):
#     sub_group_id = models.ForeignKey(ProductsSubGroup, on_delete=models.CASCADE)
#     product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
#     attr_value = models.ForeignKey(AttrValue, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'{self.product_id} - {self.attr_value}'


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_sum_tax(self):
        return sum(basket.sum() for basket in self) + 10

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class UserShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def sum(self):
        return self.product.price * self.quantity

    def increment_quantity(self):
        self.quantity += 1

    def checkout_json(self):
        data = {
            'product_id': self.product.id,
            'product': self.product.name,
            'quantity': self.quantity,
            'price': round(self.product.price),
            'sum': round(self.sum())
        }
        return data
