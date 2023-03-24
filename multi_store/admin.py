from django.contrib import admin

from .models import *


# Register your models here.
# class AttrInline(admin.StackedInline):
#     model = ProductAttribute


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductsCategories)
class ProductsCategoriesAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductsSubGroup)
class ProductsSubGroupAdmin(admin.ModelAdmin):
    pass


# @admin.register(TypicalProductAttr)
# class TypicalProductAttrAdmin(admin.ModelAdmin):
#     pass


@admin.register(ResolutionAttrValue)
class ResolutionAttrValueAdmin(admin.ModelAdmin):
    pass


@admin.register(LensAttrValue)
class LensAttrValueAdmin(admin.ModelAdmin):
    pass


@admin.register(IRAttrValue)
class IRAttrValueAdmin(admin.ModelAdmin):
    pass


@admin.register(CaseAttrValue)
class CaseAttrValueAdmin(admin.ModelAdmin):
    pass


# @admin.register(ProductAttribute)
# class ProductAttributeAdmin(admin.ModelAdmin):
#     pass


@admin.register(UserShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    pass


@admin.register(IPProductAttr)
class IPProductAttrAdmin(admin.ModelAdmin):
    pass
