from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

from products.models import Product


# def api_home(request):
    
#     data = Product.objects.all().order_by('?').first()
  
#     try:
#         data = model_to_dict(data, fields=['title', 'price'])
#     except:
#         pass


#     # print(request.headers)
#     # print(request.content_type)
#     # print(request.scheme)
#     # print(request.user)

#     return JsonResponse(data)


# ---------------------------------------------------------------------------------------------------------------

# Using drf.

# @api_view(['GET'])
# def api_home(request):

    
    
#     data = Product.objects.all().order_by('?').first()

#     try:
#         # data = model_to_dict(data, fields=['title', 'price', 'sale_price']) # sale_price is a property in the model. it wont be in the model fields.

#         # Using serializer
#         serialized_data = ProductSerializer(data).data
#     except:
#         pass

#     # return Response(data)
#     return Response(serialized_data)

# ---------------------------------------------------------------------------------------------------------------

@api_view(['POST'])
def api_home(request):

    serialized_data = ProductSerializer(data=request.data)
    
    if serialized_data.is_valid(raise_exception=True):
            # inst = serialized_data.save()
            # print(inst)
        print(serialized_data.data)
   
        # return Response(data)
        return Response(serialized_data.data)
    
    # return Response({}, status=400)


