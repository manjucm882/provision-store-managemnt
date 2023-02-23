from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from . serializers import ProductSerializer
from . models import Product
     

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/product-list/',
        'Detail View' : '/product-detail/<int:id>',
        'Create' : '/product-create/',
        'Update' : '/product-update/<int:id>',
        'Delete' : '/product-detail/<int:id>',

    }

    return Response(api_urls);

# for all products
   
@api_view(['GET'])
def ShowAll(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products,many = True)
    return Response(serializer.data)


# for individual product

@api_view(['GET'])
def ViewProduct(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product,many=False)
    return Response(serializer.data)

# for create products

@api_view(['POST'])
def CreateProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

# for updating product

@api_view(['POST'])
def UpdateProduct(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance = product,data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

# for Deleting Product

@api_view(['GET'])
def DeleteProduct(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()

    return Response('Items deleted Successfully')

