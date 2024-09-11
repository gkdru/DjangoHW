from rest_framework import serializers
from .models import Good, KaspiShop


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = "__all__"


class KaspiSerializer(serializers.ModelSerializer):
    class Meta:
        model = KaspiShop
        fields = "__all__"
