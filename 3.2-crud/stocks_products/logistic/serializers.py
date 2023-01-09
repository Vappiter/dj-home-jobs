from rest_framework import serializers
from .models import Product, Stock, StockProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title','description']
        
 
class ProductPositionSerializer(serializers.ModelSerializer):
         
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']
    # настройте сериализатор для позиции продукта на складе
    


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']
        
    # настройте сериализатор для склада

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)
        for position in positions:
          position["stock"] = stock
          StockProduct.objects.create(**position)
        return stock    
        
        # создаем склад по его параметрам
        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

       

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        print(positions)
        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)
        # print (stock)
        for position in positions:
          print (position)
        #   if position[0][1] == product.pk:
        #     print (position)  
          StockProduct.objects.update(stock_id=stock.pk,**position)
        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        return stock
