from django.db import models

class ProductType(models.Model):
    titel = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
   # create_time = models.TimeField(auto_now_add=True)
   # modified_time = models.TimeField(auto_now=True)

    class Meta:
        verbose_name = 'ProductType'
        verbose_name_plural = 'ProductType'



    def __str__(self) -> str:
        return self.titel


class ProductAttribute(models.Model):
    INTEGER = 1
    STRING = 2
    FLOAT = 3
    ATTRIBUTE_TYPE_FIELDS = (
        (INTEGER, 'Integer'),
        (STRING, 'String'),
        (FLOAT, 'Float'),
    )
    title = models.CharField(max_length=50)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='attributes')
    attribute_type = models.PositiveSmallIntegerField(default=INTEGER, choices=ATTRIBUTE_TYPE_FIELDS)


    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name



class Brand(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,blank=True, null=True, related_name='children')

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT, related_name='products')
    ups = models.BigIntegerField(unique=True)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='products')


    def __str__(self) -> str:
        return self.title




class ProductAttributeValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attribute_values')
    value = models.CharField(max_length=50)
    attribute = models.ForeignKey(ProductAttribute, on_delete=models.PROTECT, related_name='values')

    def __str__(self) -> str:
        return f'{self.product}({self.attribute}):{self.value}'

