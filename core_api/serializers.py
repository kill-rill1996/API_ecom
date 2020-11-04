from rest_framework import serializers
from core.models import Item, Category, OrderItem, Order


class ItemListSerializer(serializers.ModelSerializer):
    """Сериализация всех товаров"""
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Item
        fields = ('id', 'title', 'category', 'price', 'discount_price')


class ItemDetailSerializers(serializers.ModelSerializer):
    """Сериализация одного определнного товара"""

    class Meta:
        model = Item
        fields = ('id', 'title', 'category', 'slug', 'description', 'price', 'discount_price', 'created', 'image')


class CategoryListSerializer(serializers.ModelSerializer):
    """Список всех категорий"""
    items_count = serializers.IntegerField()

    class Meta:
        model = Category
        fields = ('id', 'title', 'items_count')


class CategoryItemsSerializer(serializers.ModelSerializer):
    """Сериализует поля для вещей в данной категории"""

    class Meta:
        model = Item
        fields = ('title', 'price', 'discount_price', 'image')


class CategoryDetailSerializer(serializers.ModelSerializer):
    """Сериализатор выбранной категории"""

    items = CategoryItemsSerializer(many=True, read_only=True)
    count = serializers.IntegerField()

    class Meta:
        model = Category
        fields = ('title', 'count', 'items')


class OrderItemSerializer(serializers.ModelSerializer):
    item = serializers.SlugRelatedField(slug_field='title', read_only=True)
    item_id = serializers.ReadOnlyField(source='item.id')
    item_price = serializers.ReadOnlyField(source='item.price')
    item_discount_price = serializers.ReadOnlyField(source='item.discount_price')

    class Meta:
        model = OrderItem
        fields = ('item_id', 'item', 'quantity', 'item_price', 'item_discount_price', 'total_amount')


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'user', 'start_date', 'items', 'total_order_amount', 'ordered')

