from rest_framework import viewsets
from api.serializers import ProductSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Products


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('name',)
    ordering = ('-name',)
