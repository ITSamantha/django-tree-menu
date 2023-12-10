from django.contrib import admin

from django.contrib import admin
from menu.models import Menu, MenuItem
from menu.inlines import MenuItemInline

LIST_PER_PAGE = 10


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'parent', 'url')
    list_editable = ('title', 'parent', 'url')

    list_per_page = LIST_PER_PAGE

    list_display_links = ('id',)

    show_full_result_count = True

    ordering = ('id',)

    search_fields = ('title', 'url')

    list_filter = ('parent',)

    inlines = [MenuItemInline, ]


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_editable = ('title',)

    list_per_page = LIST_PER_PAGE

    list_display_links = ('id',)

    show_full_result_count = True

    ordering = ('id',)

    search_fields = ('title',)

    filter_horizontal = ('items',)
