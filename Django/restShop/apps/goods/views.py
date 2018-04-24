from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from .serializers import GoodsSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics

from rest_framework import viewsets

from goods.models import Goods

class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100

# class GoodsListView(mixins.ListModelMixin, generics.GenericAPIView):
#     """
#     商品列表页
#     """
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializers
#     pagination_class = GoodsPagination
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表页
    """
    # queryset = Goods.objects.all()
    serializer_class = GoodsSerializers
    pagination_class = GoodsPagination

    def get_queryset(self):
        return Goods.objects.filter(shop_price__gt=100)
