from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact = models.TextField()

    def __str__(self):
        return str(self.name)


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateField(auto_now_add=True)
    suppliers = models.ManyToManyField(Supplier, related_name="items")

    def __str__(self):
        return str(self.name)
