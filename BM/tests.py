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
#             test2 = Test2.objects.all()
#             resuilt_page =pagination.paginate_queryset(test2,request)
#             serializers = Test2Serializer(resuilt_page,many = True)
#             return Response(serializers.data)


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


















