from django.contrib import admin
from menu.models import MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1
