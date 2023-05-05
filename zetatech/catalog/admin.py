from django.contrib import admin
from .models import Product, CategoryProduct, Tag
# Register your models here.

@admin.register(CategoryProduct)
class CategoryProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',),}
    save_as = True
    save_on_top = True

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',),}
    save_as = True


admin.site.register(Tag)
