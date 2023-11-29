from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from .models import Product

# @api_view(['GET'])
# def apiOverview(requets):
#     api_urls = {
#         'List' : '/product-list/',
#         'Detail View':'/product-detail/<int:id>',
#         'Create' : '/product-create/',
#         'Update' : '/product-update/<int:id>',
#         'Delete' : '/product-detail/<int:id>',
#     }

#     return Response(api_urls)

@api_view(['GET'])
def showAll(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ViewProduct(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CreateProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def UpdateProduct(request,pk):
    products = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=products,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def DeleteProduct(request,pk):
    products = Product.objects.get(id=pk)
    products.delete()

    return Response('Items Deleted Successfully!')