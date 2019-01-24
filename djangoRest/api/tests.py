from django.test import TestCase
from model_mommy import mommy

from .models import Products


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
