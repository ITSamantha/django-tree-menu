from django.contrib import admin
from menu.models import MenuItem


# Product Inlines
class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1

