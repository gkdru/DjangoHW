from django.contrib import admin
from .models import KaspiShop, ShopGoods, Good, Review
# Register your models here.
admin.site.register(KaspiShop)
admin.site.register(ShopGoods)
admin.site.register(Good)
admin.site.register(Review)