from django.contrib import admin

from core.models import Item, Category, ItemImage, Order, OrderItem, WishItem, Reviews


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Item)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(ItemImage)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(WishItem)
admin.site.register(Reviews)