from rest_framework import serializers
from rest_framework.exceptions import ValidationError
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
        for i in validated_data:
            print(i)
        stock = super().create(validated_data)
        for position in positions:
            stock_product = StockProduct(
                stock=stock,
                product=position['product'], 
                quantity=position['quantity'],
                price=position['price'] 
            ).save()
        return stock    
        
        # создаем склад по его параметрам
        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

       

    def update(self, instance, validated_data):
        try:
            positions = validated_data.pop('positions')
            print (positions)
        except KeyError:
            positions = []
        stock = super().update(instance, validated_data)
        try: 
           for position in positions:
             stock_product = StockProduct.objects.get(stock=stock, product=position.get('product'))  
             if position.get('quantity'):
              stock_product.quantity = position.get('quantity')
             if position.get('price'):
              stock_product.price = position.get('price')
             stock_product.save()
            
        except StockProduct.DoesNotExist:
             test1 = position.get('product').title
             raise ValidationError (('Продукт %s отсутствует на данном складе') % test1)
        return stock        
        
