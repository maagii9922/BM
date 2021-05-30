from django.db.models import fields
from rest_framework import serializers
from .models import Category, Product,ProdType,State,Company,Customer
from BM import models

class ProductSerializer(serializers.ModelSerializer):
    comName = serializers.CharField(source='company.comName')
    # hayag = serializers.CharField(source='company.hayag')
    # phone = serializers.CharField(source='company.phone')
    catName = serializers.CharField(source='category.catName')
    typeName = serializers.CharField(source='prodType.typeName')
    stateName = serializers.CharField(source='state.stateName')

    class Meta:
        depth = 1
        model = Product

        fields = [
            "prodName",
            "zCode",
            "typeName",
            "zzCode",
            "price",
            "hemNegj",
            "hudNegj",
            "comName",
            # "hayag",
            # "phone",
            "erNershil",
            "emHelber",
            "paiz",
            "uildwerlegch",
            "uNiiluulegch",
            "catName",
            "borBoloh",
            "hudAwch",
            "stateName",
        ]


class CompanySerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many = True)

    class Meta:
        depth = 1
        model = Company

        fields = [
            "comName",
            "hayag",
            "phone",
            "products"
        ]

class CategorySerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many = True)

    class Meta:
        depth = 1
        model = Category

        fields = [
            "catName",
            "products"
        ]

class ProdTypeSerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many = True)

    class Meta:
        depth = 1
        model = ProdType

        fields = [
            "typeName",
            "products"
        ]


class StateSerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many = True)

    class Meta:
        depth = 1
        model = State

        fields = [
            "stateName",
            "products"
        ]

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        depth = 1
        model = Customer

        fields = [
            "name",
            "code",
            "mail",
            "password",
        ]









