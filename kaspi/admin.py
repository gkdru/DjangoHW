from django.contrib import admin
from .models import Shop, ShopGoods, Good
# Register your models here.
admin.site.register(Shop)
admin.site.register(ShopGoods)
admin.site.register(Good)