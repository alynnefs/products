from rest_framework.request import Request
from rest_framework.test import (
    APIRequestFactory,
    APITestCase
)
from django.test import TestCase
from model_mommy import mommy

from .models import Products
from .serializers import ProductSerializer


class BaseViewTest(APITestCase):
    """
    This class creates test data
    """

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
    """
    This class tests data creation
    """
    def test_get_all_products(self):
        print("\nget products")

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


class TestProductsModels(TestCase):
    """
    This class tests create, delet and update
    """
    def test_create_products(self):
        """
        This method tests if the objects were created
        """
        print("\ncreate objects")

        before = Products.objects.count()
        mommy.make(Products)
        after = Products.objects.count()
        self.assertEqual(before+1, after)

    def test_delete_products(self):
        """
        This method tests if the objects were deleted
        """
        print("\ndelete objects")

        mommy.make(Products, _quantity=3)
        before = Products.objects.count()
        
        id = Products.objects.first().id
        Products.objects.filter(id=id).delete()  

        after = Products.objects.count()
        self.assertEqual(before-1, after)

    def test_update_products(self):
        """
        This method tests if the objects were updated
        """
        print("\nupdate objects")

        name = 'caderno'
        new_name = 'livro'
        mommy.make(Products, name=name)
        before = Products.objects.first().name

        Products.objects.filter(name=name).update(name=new_name)
        after = Products.objects.first().name

        self.assertNotEqual(before, after)
        self.assertEqual(after, 'livro')
