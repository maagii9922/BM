from django.http import HttpResponse
from rest_framework import pagination
from rest_framework import serializers
from rest_framework.serializers import Serializer
from .models import Category, Customer, Product,Company,State,ProdType
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import ProductSerializer,CompanySerializer,CustomerSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import status


def home(request):
    # products = Product.objects.get(state = 1)
    # products.save()
    # print(products)

    # products = Product.objects.get(state = 1)
    # states = State.objects.get(stateName = 'tsu')
    # products.state = states
    # products.save()
    # print(products)

    # products = Product.objects.get(pk=1)
    # company = Company.objects.get(comName = 'w')
    # products.company = company
    # products.save()
    # print(products)

    # customer = Customer.objects.get(company = 1)
    # company = Company.objects.get(comName = 'w')
    # company.save()
    # customer.company = company
    # customer.save()
    # print(customer)
    
    # company = Company(comName = 'sss', hayag = 'ss', phone = 999)
    # company.save()
    # customer = Customer.objects.get(pk = 1)
    # customer.company = company
    # customer.save()
    # print(customer)

    # company = Company(comName = 'sss', hayag = 'ss', phone = 999)
    # company.save()
    # customer = Customer.objects.get(pk = 1)
    # customer.company = company
    # customer.save()
    # print(customer)
    
    # company = Company(comName = 'qq', hayag = 'qq', phone = 333)
    # company.save()
    # customer = Customer(name = 'nomuka',code = '12',company = company,mail = 'nnn',password = '2112')
    # customer.save()
    # print(customer)

    category = Category (catName = 'dd')
    category.save()
    prodType = ProdType (typeName = 'buts')
    prodType.save()
    state = State (stateName = 'ccc')
    state.save()
    company = Company(comName = 'qq', hayag = 'qq', phone = 333)
    company.save()
    customer = Customer(name = 'nomuka',code = '12',company = company,mail = 'nnn',password = '2112')
    customer.save()
    products = Product (prodName = 'xx',zCode = 12,prodType = prodType,zzCode = 1212,price = 2323,hemNegj = 1,hudNegj = 1,company = company,erNershil = 'dd',emHelber = 'tab',paiz = 'hh',uildwerlegch = 'vvv',uNiiluulegch = 'sss',category = category,borBoloh = 'no',hudAwch = 'no',state = state)
    products.save()
    print(products)

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
def product_state(request):
        
    if request.method == "GET":
        products = Product.objects.get(state=1)
        products.save()
        print(products)
        serializer = ProductSerializer(products)
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






