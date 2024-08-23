from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.postgres.fields import DateRangeField,DateTimeRangeField,ArrayField
import datetime


now = datetime.datetime.now()
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
    example = DateTimeRangeField(verbose_name='Example')
    active_in = DateRangeField(verbose_name='Активен между', default=(now,'2024-12-12'))
    tags = ArrayField(base_field=models.CharField(max_length=30),verbose_name='Tags')

class RevKaspiShop(KaspiShop):
    class Meta:
        proxy = True,
        ordering = ['created_date']


class ShopGoods(models.Model):
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    shop = models.ForeignKey(KaspiShop, on_delete=models.CASCADE)




@receiver(post_save, sender=Good)
def post_save_dispatcher(sender, **kwargs,):
        if kwargs['created']:
            print("Товар "+kwargs['instance'].name+" был создан")


@receiver(post_delete,sender=Good)
def post_delete_dispatcher(sender, **kwargs):
        print(f"Товар {kwargs['instance'].name} удален")