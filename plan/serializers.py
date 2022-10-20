from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PlanSerializer(serializers.ModelSerializer):
    # product = ProductSerializer(read_only=True)

    class Meta:
        model = Plan
        fields = '__all__'


class ProductExpenseProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_expense_product
        fields = '__all__'

