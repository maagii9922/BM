from django.db.models import fields
from rest_framework import serializers
from .models import Product,ProdType,State,Company,Customer
from BM import models

class ProductSerializer(serializers.ModelSerializer):
    comName = serializers.CharField(source='company.comName')
    hayag = serializers.CharField(source='company.hayag')
    phone = serializers.CharField(source='company.phone')
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
            "hayag",
            "phone",
            "erNershil",
            "emHelber",
            "paiz",
            "uildwerlegch",
            "uNiiluulegch",
            "category",
            "borBoloh",
            "hudAwch",
            "stateName",
        ]


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        depth = 1
        model = Company

        fields = [
            "comName",
            "hayag",
            "phone",
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









