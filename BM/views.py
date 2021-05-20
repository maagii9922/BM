from django.http import HttpResponse
from rest_framework import pagination
from rest_framework import serializers
from rest_framework.serializers import Serializer
from .models import Customer, Product,Company,State,ProdType
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import ProductSerializer,CompanySerializer,CustomerSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import status


def home(request):
    return HttpResponse("hello")

@api_view(["GET"])
@permission_classes([])
def product_list(request):
    if request.method == "GET":
        pagination = PageNumberPagination()
        if 'size' in request.GET:
            pagination.page_size = request.GET['size']
        products = Product.objects.all()
        result_page = pagination.paginate_queryset(products,request)
        serializer = ProductSerializer(result_page, many=True)
        return Response(serializer.data)

@api_view(["GET"])
@permission_classes([])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == "GET":
        serializer = ProductSerializer(product)
        return Response(serializer.data)

@api_view(["GET"])
@permission_classes([])
def company_list(request):
    if request.method == "GET":
        company = Company.objects.all()
        serializer = CompanySerializer(company,many=True)
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([])
def customer_list(request):
    if request.method == "GET":
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer,many=True)
        return Response(serializer.data)






