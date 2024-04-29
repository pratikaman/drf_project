from django.shortcuts import render
from .models import Product
import requests
from django.http import JsonResponse
from rest_framework import generics
from .serializers import ProductSerializer

def populate_products(request):
    
    products = Product.objects.all()
    products_count = Product.objects.count()

    if products_count == 0:
        response = requests.get('https://fakestoreapi.com/products')
        data = response.json()

        for product in data:
            Product.objects.create(
                title=product['title'],
                content=product['description'],
                price=product['price']
            )

        return JsonResponse({'message': 'Products populated successfully!'})
    
    return JsonResponse({'message': 'Products already populated!'})




