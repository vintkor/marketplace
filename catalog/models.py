from django.db import models
from django.utils.crypto import get_random_string
from marketplace.basemodel import BaseModel
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from finance.models import Currency
from params.models import Vendor


def set_product_image_name(instanse, filename):
    name = get_random_string(20)
    ext = filename.split('.')[-1]
    path = 'images/catalog/products/{}__{}.{}'.format(instanse.pk, name, ext)
    return path


class Category(BaseModel, MPTTModel):
    parent = TreeForeignKey(
        'self', null=True, blank=True,
        related_name='children', db_index=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)

    class MPTTMeta:
        order_insertion_by = ('title',)

    def __str__(self):
        return self.title


class Product(BaseModel):
    """
    Товар - должен иметь хотя бы один вариант
    """
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    course = models.DecimalField(max_digits=10, decimal_places=5)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    main_image = models.ImageField(upload_to=set_product_image_name)

    def __str__(self):
        return self.title

    def get_variants(self):
        return self.productvariant_set.all()


class ProductVariant(BaseModel):
    """
    Вариант товара
    """
    title = models.CharField(max_length=250)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(upload_to=set_product_image_name)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return '{} {}'.format(self.product.title, self.title)

    def get_price(self):
        if self.product.currency.is_main:
            return round(self.price, 2)
        return round(self.price * self.product.course, 2)

    def get_currency(self):
        return self.product.currency

    def get_course(self):
        if self.product.currency.is_main:
            return ' '
        return self.product.course


class ProductImage(BaseModel):
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=set_product_image_name)
    alt = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.alt if self.alt else 'Not alt'
