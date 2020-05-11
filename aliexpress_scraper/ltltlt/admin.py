from django.contrib import admin

# Register your models here.
from .models import Price, Item

class PriceInline(admin.TabularInline):
    model = Price

class ItemAdmin(admin.ModelAdmin):
    inlines = [PriceInline]
    list_filter = ['created_date']
    search_fields = ['item_name']

admin.site.register(Item, ItemAdmin)