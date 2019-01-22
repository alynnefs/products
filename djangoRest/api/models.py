from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=255, null=False)
    price = models.FloatField(null=False, blank=False)
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return "{} - {} - {}".format(self.name, self.price, self.description)
        