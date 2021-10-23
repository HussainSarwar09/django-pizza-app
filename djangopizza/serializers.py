from django.db import models
from rest_framework import serializers
from django_filters import rest_framework
from .models import Size, Topping, Pizza


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = '__all__'


class PizzaSerializer(serializers.ModelSerializer):
    size = SizeSerializer(many=False)
    toppings = ToppingSerializer(many=True)
    class Meta:
        model = Pizza
        fields = ('id', 'name', 'type', 'size', 'toppings')
        # depth = 1

    def validate(self, attrs):
        return super().validate(attrs)



class PizzaSizeFilter(rest_framework.FilterSet):
    size = rest_framework.CharFilter(field_name='size__name', lookup_expr='iexact')

    class Meta:
        fields = ('size', 'type')
        model = Pizza