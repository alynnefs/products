from rest_framework import viewsets
from api.serializers import ProductSerializer

from .models import Products


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
