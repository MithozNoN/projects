from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Products, Order, Seccion
# Register your models here.

admin.site.site_header = "Jaguarete Kaa S.A."
admin.site.site_title = "Jaguarete Kaa S.A."
admin.site.index_title = "Panel de administración"

class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")
    change_category_to_default.short_description = 'Default Category'
    list_display = ('title','price','seccion','description','image')
    search_fields = ('title',)
    actions = ('change_category_to_default',)
    list_editable = ('price',)
    
admin.site.register(Products,ProductAdmin)
admin.site.register(Order)
admin.site.register(Seccion)