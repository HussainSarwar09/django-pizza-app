from django import urls
from django.urls import path, include
from rest_framework import routers
from .views import (
    SizeViewSet, 
    ToppingViewSet, 
    PizzaViewSet,
)

router = routers.DefaultRouter()
router.register('api/size', SizeViewSet)
router.register('api/topping', ToppingViewSet)
router.register('api/pizza', PizzaViewSet, basename='pizza')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
