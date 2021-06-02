from django.db.models.base import Model
from rest_framework import pagination
from BM.models import Test,Test2
from django.db import models
from django.db.models import fields
from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.utils.translation import ugettext_lazy as _
from rest_framework.pagination import PageNumberPagination


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

class Test(model.Model):
    m = models.CharField(max_length=50)
    v = models.CharField(max_length=50,verbose_name=_("kkkk"))

    class Meta:
        verbose_name = _("hhhhh")

class TestSerializer(serializers.ModelSerializer):

    class Meta:
        depth = 1
        model  = Test
        fields = "__all__"

@api_view(["GET"])
@permission_classes([])
def test_list(request):
    if request.method == "GET":
        test = Test.objects.all()
        serializer = TestSerializer(test, many=True)
        return Response(serializer.data)



@api_view(["GET"])
@permission_classes([])
def test_detail(request,pk):
    try:
        test = Test.objects.get(pk=pk)
    except Test.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":        
        serializer = TestSerializer(test)
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([])
def test_detial2(request, pk):
    if request.method == "GET":
        pagination = PageNumberPagination()
        if 'size' in request.GET:
            pagination.page_size = request.GET['size']
        test = Test.objects.all()
        result_page = pagination.paginate_queryset(test, request)
        serializer = TestSerializer(result_page, many=True)
        return Response(serializer.data) 




# class Test2(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self) :
#         return self.name

# class Test2Serializer(serializers.ModelSerializer):
#     class Meta:
#         depth: 1
#         model: Test2
#         fields: "__all__"
        

# @api_view(["GET"])
# @permission_classes([])
# def test2(request):
#     if request.method == "GET":
#         test2 = Test2.objects.all()
#         serializers = Test2Serializer(test2,many = True)
#         return Response(serializers.data)


# @api_view(["GET"])
# @permission_classes([])
# def test2_detail(request,pk):
#     try:
#         test2 = Test2.objects.get(pk=pk)
#     except Test2.DoesNotExist:
#         return Response(status = status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializers = Test2Serializer(test2)
#         return Response(serializers.data)


# @api_view(["GET"])
# @permission_classes([])
# def test2_detail2(request):
#     if request.method == "GET":
#         pagination = PageNumberPagination()
#         if 'size' in request.GET:
#             pagination.page_size = request.GET['size']
#             test2 = Test2.objects.all()
#             result_page = pagination.paginate_queryset(test2,request)
#             serializers = Test2Serializer(result_page,many = True)
#             return Response(serializers.data)
    
# @api_view(["GET"])
# @permission_classes([])
# def test2_detail2(request):
#     if request.method == "GET":
#         pagination = PageNumberPagination()
#         if 'size' in request.GET:
#             pagination.page_size = request.GET['size']
#         test2 = Test2.objects.all()
#         resuilt_page =pagination.paginate_queryset(test2,request)
#         serializers = Test2Serializer(resuilt_page,many = True)
#         return Response(serializers.data)


# class Test2(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self) :
#         return self.name

# class Test2Serializer(serializers.ModelSerializer):
#     class Meta:
#         depth: 1
#         model: Test2
#         fields: "__all__"
        

# @api_view(["GET"])
# @permission_classes([])
# def test2(request):
#     if request.method == "GET":
#         test2 = Test2.objects.all()
#         serializers = Test2Serializer(test2,many = True)
#         return Response(serializers.data)


# @api_view(["GET"])
# @permission_classes([])
# def test2_detail(request,pk):
#     try:
#         test2 = Test2.objects.get(pk=pk)
#     except Test2.DoesNotExist:
#         return Response(status = status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializers = Test2Serializer(test2)
#         return Response(serializers.data)

# @api_view(["GET"])
# @permission_classes([])
# def product_list(request):
#     """
#     List all code products, or create a new snippet.
#     """
#     if request.method == "GET":
#         paginator = PageNumberPagination()
#         if 'size' in request.GET:
#             paginator.page_size  = request.GET['size']
#         products = Product.objects.all()
#         result_page = paginator.paginate_queryset(products, request)

#         serializer = ProductSerializer(result_page, many=True)
#         # serializer = ProductSerializer(products, many=True)
       
#         return Response(serializer.data)






# @api_view(["GET","POST"])
# @permission_classes([])
# def category_list(request):
#     if request.method == "GET":
#         category = Category.objects.all()
#         serializer = CategorySerializer(category,many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)














