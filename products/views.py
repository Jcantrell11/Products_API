from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework import status
from .models import Product

# Create your views here.

@api_view(['GET'])
def products_list(request):
    products = Product.objects.all()

    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
