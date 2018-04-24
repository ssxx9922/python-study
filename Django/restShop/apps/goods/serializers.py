#_*_ coding:utf-8 _*_
__author__ = 'Harryue'
__date__ = '2018/4/24 AM10:56'

from rest_framework import serializers
from goods.models import Goods,GoodsCategory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = '__all__'

class GoodsSerializers(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Goods
        fields = '__all__'