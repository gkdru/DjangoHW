from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

# Create your models here.
class Review(models.Model):
    text = models.TextField(max_length=1000)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(ct_field='content_type',
                                       fk_field='object_id')
    
class GoodManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().order_by('price', 'name')
    def price_filter(self) -> models.QuerySet:
        return super().get_queryset().filter(price__gt=200)

class Good(models.Model):
    name = models.TextField(max_length=250, default="good")
    description = models.TextField(max_length=250)
    price = models.IntegerField(null=False)
    objects = GoodManager()
    reviews = GenericRelation('Review', default='123')
    def __str__(self) -> str:
        return self.name

class Shop(models.Model):
    created_date = models.DateField(auto_now_add=True)
    goods = models.ManyToManyField(to=Good,through="ShopGoods", through_fields=("shop", "good"))
    staff = models.ManyToManyField(to=User)
    reviews = GenericRelation('Review', default='123')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        abstract = True

class KaspiShop(Shop):
    name = models.TextField(max_length=250)
    

class RevKaspiShop(KaspiShop):
    class Meta:
        proxy = True,
        ordering = ['created_date']


class ShopGoods(models.Model):
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    shop = models.ForeignKey(KaspiShop, on_delete=models.CASCADE)



