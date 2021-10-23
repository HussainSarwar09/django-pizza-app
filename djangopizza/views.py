from django.db.models import query, query_utils
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import Size, Topping, Pizza
from rest_framework import viewsets
from .serializers import PizzaSizeFilter, SizeSerializer, ToppingSerializer, PizzaSerializer
import requests
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import APIException



class SizeViewSet(viewsets.ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer


class ToppingViewSet(viewsets.ModelViewSet):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer


class PizzaViewSet(viewsets.ModelViewSet):
    serializer_class = PizzaSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PizzaSizeFilter
    
    def get_queryset(self):
        queryset = Pizza.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if not serializer:
                raise APIException('There was a problem with initialising serializer!')

            # Serializer data validation cehck
            if not serializer.is_valid():
                error = serializer.errors
                raise APIException('Serializer data is not valid! Please check the below errors and try again. '\
                                    f'Error Field: {list(error.keys())[0]}; Error Message: {list(error.values())[0][0]}')

            validated_data = serializer.validated_data

            # Fetch size object
            size = Size.objects.filter(name=validated_data.get('size').get('name'))
            if not size.exists() or not size:
                valid_sizes = [size.name for size in Size.objects.all()]
                raise APIException('Invalid entry in size field. Please check again.')

            # create pizza object
            pizza_object = Pizza.objects.create(
                name = validated_data.get('name'),
                type = validated_data.get('type'),
                size = size.first()
            )

            # add topping object to pizza object
            toppings_list = validated_data.get('toppings')
            for topping in toppings_list:
                topping_obj, created = Topping.objects.get_or_create(name=topping.get('name'))
                pizza_object.toppings.add(topping_obj)

            return redirect(f'/api/pizza/{pizza_object.id}/')

        except Exception as e:
           return JsonResponse({'error' : str(e)}, status=400)


    def update(self, request, *args, **kwargs):
        try:
            url_params = self.kwargs
            pizza_id = url_params.get('pk')
            pizza_instance_filter = Pizza.objects.filter(id=pizza_id)
            if not pizza_instance_filter:
                raise APIException(f'No valid pizza entry exists for the id specified.')

            # fetch pizza object to update
            pizza_instance = pizza_instance_filter.first()
            serializer = self.serializer_class(pizza_instance, data=request.data)
            if not serializer:
                raise APIException('There was a problem with initialising serializer!')

            # Serializer data validation check
            if not serializer.is_valid():
                error = serializer.errors
                raise APIException('Serializer data is not valid! Please check the below errors and try again. '\
                                        f'Error Field: {list(error.keys())[0]}; Error Message: {list(error.values())[0][0]}')

            validated_data = serializer.validated_data

            # Update name
            pizza_instance.name = validated_data.get('name')

            # Update type
            pizza_instance.type = validated_data.get('type')

            # Update Size        
            size = Size.objects.filter(name=validated_data.get('size').get('name'))
            if not size.exists():
                valid_sizes = [size.name for size in Size.objects.all()]
                raise APIException('Invalid entry in size field. '\
                    f'Valid entries are {valid_sizes}')
            pizza_instance.size = size.first()
            pizza_instance.save()

            # Get toppings from pizza instance
            toppings_pizza_instance = [topping for topping in pizza_instance.toppings.all()]

            # Get toppings from request
            toppings_list = validated_data.get('toppings')
            toppings_request = [Topping.objects.get(name=topping.get('name')) for topping in toppings_list]

            # Remove Toppings
            for obj in toppings_pizza_instance:
                if obj not in toppings_request:
                    pizza_instance.toppings.remove(obj)
            pizza_instance.save()

            # Add Toppings
            for obj in toppings_request:
                if obj not in toppings_pizza_instance:
                    pizza_instance.toppings.add(obj)
            pizza_instance.save()                

            return redirect (f'/api/pizza/{pizza_id}/') 

        except Exception as e:
            return JsonResponse({'error' : str(e)}, status=400)
