from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(CheckoutOrder)
class CheckOutAdmin(admin.ModelAdmin):
    list_display = ['initiator', 'created']
    readonly_fields = ['initiator']


@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']
