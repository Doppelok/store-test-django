from django.contrib import admin
from .models import EmailNews


# Register your models here.

@admin.register(EmailNews)
class EmailNewsAdmin(admin.ModelAdmin):
    list_display = ['email', 'status']
