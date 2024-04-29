from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        # fields = "__all__"
        fields = [
            'title', 
            'price', 
            'sale_price', # sale_price is a property in the model. But we can serialize it.
            # 'get_discount' # get_discount is a method in the model. But we can serialize it.
            'my_discount'
            ] 
        
    def get_my_discount(self, obj):
        # obj is the instance of the model.
        # try:
        #     return obj.get_discount()
        # except:
        #     return None
        
        if not hasattr(obj, 'id'):
            return None
        
        if not isinstance(obj, Product):
            return None 
        
        return obj.get_discount()