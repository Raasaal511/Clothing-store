from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models as md


@admin.register(md.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('preview_image', 'title', 'brand', 'sum')
    fields = ('title', 'brand', 'description', 'tags', 'sizes', 'gender', 'season', 'image',
              'preview_image', 'price', 'slug')
    list_display_links = ('title', 'brand', 'sum')
    readonly_fields = ['preview_image']
    prepopulated_fields = {'slug': ('title',)}
    classes = ('grp-collapse grp-open',)

    def preview_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width=90 height=70>')

    def sum(self, obj):
        return mark_safe(f'{obj.price}$')


@admin.register(md.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(md.Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('sizes_latin', 'numeric_size')
    list_display_links = ('sizes_latin', 'numeric_size')


@admin.register(md.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(md.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'email', 'address', 'date_created')
    list_display_links = ('user', 'phone', 'email', 'address')
