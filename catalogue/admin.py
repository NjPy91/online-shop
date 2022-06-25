from itertools import product
from unicodedata import category
from django.contrib import admin
from catalogue.models import Category, Brand, Product, ProductAttribute, ProductAttributeValue, ProductType




admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(ProductAttribute)
admin.site.register(ProductAttributeValue)
admin.site.register(ProductType)
