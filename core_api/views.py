from django.conf import settings
from django.utils import timezone
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from django.db import models

from core.models import Item, Category, OrderItem, Order
from .serializers import (
    ItemListSerializer,
    ItemDetailSerializers,
    CategoryListSerializer,
    CategoryDetailSerializer,
    OrderItemSerializer,
    OrderSerializer,
)
from .service import ItemFilter, PaginationItem


class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод товаров"""

    filter_backends = (DjangoFilterBackend,)
    filterset_class = ItemFilter
    # pagination_class = PaginationItem
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        items = Item.objects.filter().order_by('category')
        return items

    def get_serializer_class(self):
        if self.action == "list":
            return ItemListSerializer
        elif self.action == "retrieve":
            return ItemDetailSerializers


# class CategoryListView(generics.ListAPIView):
#     """Вывод категорий товаров"""
#
#     queryset = Category.objects.all()
#     serializer_class = CategoryListSerializer
#
#
# class CategoryDetailView(generics.RetrieveAPIView):
#     """Вывод выбранной категории"""
#
#     queryset = Category.objects.all().annotate(
#         count=models.Count('items')
#     )
#     serializer_class = CategoryDetailSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):

    def get_queryset(self):
        categories = Category.objects.all().annotate(
            items_count=models.Count('category_items')
        )
        return categories

    def get_serializer_class(self):
        if self.action == 'list':
            return CategoryListSerializer
        if self.action == 'retrieve':
            return CategoryDetailSerializer


class OrderListView(generics.ListAPIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(ordered=False, user=self.request.user)


class OrderDetailView(APIView):

    def get(self, request, pk):
        try:
            instance = OrderItem.objects.get(item_id=pk, user=request.user, ordered=False).item
        except OrderItem.DoesNotExist:
            return Response(status=404)
        serializer = ItemDetailSerializers(instance)
        return Response(serializer.data)

    def post(self, request, pk):
        try:
            item = Item.objects.get(id=pk)
        except Item.DoesNotExist:
            return Response(status=404)
        order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)
        order_qs = Order.objects.filter(user=request.user, ordered=False)
        if order_qs.exists():
            order = order_qs[0]
            if order.items.filter(item__slug=item.slug).exists():
                order_item.quantity += 1
                order_item.save()
                return Response(status=201)
            else:
                order.items.add(order_item)
                return Response(status=201)
        else:
            ordered_date = timezone.now()
            order = Order.objects.create(user=request.user, ordered_date=ordered_date)
            order.items.add(order_item)
            return Response(status=201)

    def delete(self, request, pk):
        item = get_object_or_404(Item, id=pk)
        order_qs = Order.objects.filter(user=request.user, ordered=False)
        if order_qs.exists():
            order = order_qs[0]
            if order.items.filter(item__slug=item.slug).exists():
                order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
                if order_item.quantity == 1:
                    order.items.remove(order_item)
                    order_item.delete()
                    return Response(status=204)
                else:
                    order_item.quantity -= 1
                    order_item.save()
                return Response(status=204)
            else:
                return Response(status=204)
        else:
            return Response(status=204)

