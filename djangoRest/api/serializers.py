from rest_framework import serializers

from .models import Products


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = ('url', 'name', 'price', 'description')
