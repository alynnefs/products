from django.db import models


class Products(models.Model):
    """
    This class defines a Product model.

    :cvar str name: Product's name
    :cvar float price: Product's price
    :cvar str description: Product's description
    """
    name = models.CharField(max_length=255, null=False)
    price = models.FloatField(null=False, blank=False)
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return "{} - {} - {}".format(self.name, self.price, self.description)
        