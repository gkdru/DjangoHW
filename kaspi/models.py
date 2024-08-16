from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Good(models.Model):
    name = models.TextField(max_length=250, default="good")
    description = models.TextField(max_length=250)
    price = models.IntegerField(null=False)
    def __str__(self) -> str:
        return self.name

class Shop(models.Model):
    name = models.TextField(max_length=250)
    created_date = models.DateField(auto_now_add=True)
    staff = models.ManyToManyField(to=User)
    goods = models.ManyToManyField(to=Good,through="ShopGoods", through_fields=("shop", "good"))

    def __str__(self) -> str:
        return self.name


class ShopGoods(models.Model):
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
