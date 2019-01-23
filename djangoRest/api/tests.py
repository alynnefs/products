from rest_framework.request import Request
from rest_framework.test import (
    APIClient,
    APIRequestFactory,
    APITestCase
)

from .models import Products
from .serializers import ProductSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_product(name="", price="", description=""):
        if name and price and description != "":
            Products.objects.create(name=name, price=price,
                                    description=description)

    def setUp(self):
        # add test data
        self.create_product("Caderno", 10.50, "Capa de bolinhas")
        self.create_product("Livro", 20, "Usado")
        self.create_product("Caneta", 1.50, "Tinta azul")
        self.create_product("Lapiseira", 2, "Grafite 0.5")


class GetAllProductsTest(BaseViewTest):
    def test_get_all_products(self):

        factory = APIRequestFactory()
        request = factory.get('/')
        serializer_context = {'request': Request(request)}

        product = Products.objects.first()

        response = ProductSerializer(instance=product,
                                     context=serializer_context)

        # fetch the data from db
        expected = Products.objects.first()
        serialized = ProductSerializer(expected, context=serializer_context)
        self.assertEqual(response.data, serialized.data)    
