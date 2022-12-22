from uuid import uuid4

from django.db.models import SET_NULL, CharField, UUIDField, ForeignKey, Model, TextField, ImageField, DecimalField, \
    CASCADE
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    id = UUIDField(primary_key=True, unique=True, default=uuid4, editable=False)
    name = CharField(max_length=255)
    parent = TreeForeignKey('self', SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Shop(Model):
    id = UUIDField(primary_key=True, unique=True, default=uuid4, editable=False)
    name = CharField(max_length=255)
    description = TextField()
    image = ImageField(upload_to='shops/')


class Product(Model):
    id = UUIDField(primary_key=True, unique=True, default=uuid4, editable=False)
    name = CharField(max_length=255)
    price = DecimalField(max_digits=9, decimal_places=2)
    shop = ForeignKey('apps.Shop', CASCADE)
    category = ForeignKey('apps.Category', CASCADE)


class ProductImage(Model):
    id = UUIDField(primary_key=True, unique=True, default=uuid4, editable=False)
    image = ImageField(upload_to='shops/images/')
    product = ForeignKey('apps.Product', CASCADE)
