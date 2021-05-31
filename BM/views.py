import re
from django.core import paginator
from django.http import HttpResponse
from django.urls.resolvers import _route_to_regex
from rest_framework import pagination
from rest_framework import serializers
from rest_framework.serializers import Serializer
from .models import Category, Customer, Product,Company,State,ProdType
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import ProductSerializer,CompanySerializer,CategorySerializer,ProdTypeSerializer,StateSerializer,CustomerSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from django.db.models import Count


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
    
    # company = Company(comName = 'qq', hayag = 'qq', phone = 333)
    # company.save()
    # customer = Customer(name = 'nomuka',code = '12',company = company,mail = 'nnn',password = '2112')
    # customer.save()
    # print(customer)

    # category = Category (catName = 'dd')
    # category.save()
    # prodType = ProdType (typeName = 'buts')
    # prodType.save()
    # state = State (stateName = 'ccc')
    # state.save()
    # company = Company(comName = 'qq', hayag = 'qq', phone = 333)
    # company.save()
    # customer = Customer(name = 'nomuka',code = '12',company = company,mail = 'nnn',password = '2112')
    # customer.save()
    # products = Product (prodName = 'xx',zCode = 12,prodType = prodType,zzCode = 1212,price = 2323,hemNegj = 1,hudNegj = 1,company = company,erNershil = 'dd',emHelber = 'tab',paiz = 'hh',uildwerlegch = 'vvv',uNiiluulegch = 'sss',category = category,borBoloh = 'no',hudAwch = 'no',state = state)
    # products.save()
    # print(products)

    # products = Product.objects.get(company__id = 1)
    # print(products)

    # products = Product.objects.get(company__comName = 'qq')
    # print(products)

    return HttpResponse("hello")

"""
products
"""

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


"""
company
"""

@api_view(["GET","POST"])
@permission_classes([])
def company_list(request):
    if request.method == "GET":
        paginator = PageNumberPagination()
        # paginator.page_size = 1
        if 'size' in request.GET:
            paginator.page_size  = request.GET['size']
        company = Company.objects.all()
        result_page = paginator.paginate_queryset(company, request)
        serializer = CompanySerializer(result_page,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET","PUT","DELETE"])
@permission_classes([])
def company_detail(request,pk):
    try:
        company = Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializers =CompanySerializer(company)
        return Response(serializers.data)

    elif request.method == "PUT":
        serializers = CompanySerializer(company, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET"])
@permission_classes([])
def company_filter(request):
    # company = Company.objects.filter(comName='w', hayag='aaaaa')
    # print(request.GET)
    f = {}
    for k in request.GET:   #{'comName': ['hyg'], 'hayag': ['qq1'], 'phone': ['78']}
        # print(request.GET[k])
        f[k] = request.GET[k]   #{'comName': 'hyg', 'hayag': 'qq1', 'phone': '78'}
    # print(f)
    company = Company.objects.filter(**f)
    serializers =CompanySerializer(company,many=True)
    return Response(serializers.data)

@api_view(["GET"])
@permission_classes([])
def company_product(request,pk):
    c = Company.objects.get(pk=pk)
    # company = c.product_set.all()
    # print(company)
    serializers =CompanySerializer(c)
    return Response(serializers.data)


# @api_view(["GET"])
# @permission_classes([])
# def company_count(request):
#     company = Company.objects.filter(**f).count()

"""
category
"""

@api_view(["GET","POST"])
@permission_classes([])
def category_list(request):
    if request.method == "GET":
        paginator = PageNumberPagination()
        if 'size' in request.GET:
            paginator.page_size  = request.GET['size']
        category = Category.objects.all()
        result_page = paginator.paginate_queryset(category, request)
        serializer = CategorySerializer(result_page,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET","PUT","DELETE"])
@permission_classes([])
def category_detail(request,pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializers =CategorySerializer(category)
        return Response(serializers.data)

    elif request.method == "PUT":
        serializers = CategorySerializer(category, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET"])
@permission_classes([])
def category_filter(request):
    # company = Company.objects.filter(comName='w', hayag='aaaaa')
    # print(request.GET)
    f = {}
    for k in request.GET:   #{'comName': ['hyg'], 'hayag': ['qq1'], 'phone': ['78']}
        # print(request.GET[k])
        f[k] = request.GET[k]   #{'comName': 'hyg', 'hayag': 'qq1', 'phone': '78'}
    # print(f)
    category = Category.objects.filter(**f)
    serializers =CategorySerializer(category,many=True)
    return Response(serializers.data)

@api_view(["GET"])
@permission_classes([])
def category_product(request,pk):
    c = Category.objects.get(pk=pk)
    serializers =CategorySerializer(c)
    return Response(serializers.data)

"""
prodType
"""

@api_view(["GET","POST"])
@permission_classes([])
def prodType_list(request):
    if request.method == "GET":
        paginator = PageNumberPagination()
        if 'size' in request.GET:
            paginator.page_size  = request.GET['size']
        prodType = ProdType.objects.all()
        result_page = paginator.paginate_queryset(prodType, request)
        serializer = ProdTypeSerializer(result_page,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ProdTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET","PUT","DELETE"])
@permission_classes([])
def prodType_detail(request,pk):
    try:
        prodType = ProdType.objects.get(pk=pk)
    except ProdType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializers =ProdTypeSerializer(prodType)
        return Response(serializers.data)

    elif request.method == "PUT":
        serializers = ProdTypeSerializer(prodType, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        prodType.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET"])
@permission_classes([])
def prodType_filter(request):
    # company = Company.objects.filter(comName='w', hayag='aaaaa')
    # print(request.GET)
    f = {}
    for k in request.GET:   #{'comName': ['hyg'], 'hayag': ['qq1'], 'phone': ['78']}
        # print(request.GET[k])
        f[k] = request.GET[k]   #{'comName': 'hyg', 'hayag': 'qq1', 'phone': '78'}
    # print(f)
    prodType = ProdType.objects.filter(**f)
    serializers =ProdTypeSerializer(prodType,many=True)
    return Response(serializers.data)

@api_view(["GET"])
@permission_classes([])
def prodType_product(request,pk):
    c = ProdType.objects.get(pk=pk)
    serializers =ProdTypeSerializer(c)
    return Response(serializers.data)

"""
state
"""

@api_view(["GET","POST"])
@permission_classes([])
def state_list(request):
    if request.method == "GET":
        paginator = PageNumberPagination()
        if 'size' in request.GET:
            paginator.page_size  = request.GET['size']
        state = State.objects.all()
        result_page = paginator.paginate_queryset(state, request)
        serializer = StateSerializer(result_page,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = StateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET","PUT","DELETE"])
@permission_classes([])
def state_detail(request,pk):
    try:
        state = State.objects.get(pk=pk)
    except State.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializers =StateSerializer(state)
        return Response(serializers.data)

    elif request.method == "PUT":
        serializers = StateSerializer(state, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        state.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET"])
@permission_classes([])
def state_filter(request):
    # print(request.GET)
    f = {}
    for k in request.GET:  
        f[k] = request.GET[k]  
    state = State.objects.filter(**f)
    serializers =StateSerializer(state,many=True)
    return Response(serializers.data)

@api_view(["GET"])
@permission_classes([])
def state_product(request,pk):
    c = State.objects.get(pk=pk)
    serializers =StateSerializer(c)
    return Response(serializers.data)
"""
customer
"""
@api_view(["GET","POST"])
@permission_classes([])
def customer_list(request):
    if request.method == "GET":
        paginator = PageNumberPagination()
        if 'size' in request.GET:
            paginator.page_size  = request.GET['size']
        customer = Customer.objects.all()
        result_page = paginator.paginate_queryset(customer, request)
        serializer = CustomerSerializer(result_page,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)


@api_view(["GET","PUT","DELETE"])
@permission_classes([])
def customer_detail(request,pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializers =CustomerSerializer(customer)
        return Response(serializers.data)

    elif request.method == "PUT":
        serializers = CustomerSerializer(customer, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET"])
@permission_classes([])
def customer_filter(request):
    # print(request.GET)
    f = {}
    for k in request.GET:  
        f[k] = request.GET[k]  
    customer = Customer.objects.filter(**f)
    serializers =CustomerSerializer(customer,many=True)
    return Response(serializers.data)




