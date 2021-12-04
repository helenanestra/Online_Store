from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    created_date = models.DateTimeField(
        default=timezone.now
    )
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    class Meta:
        permissions = (("can_put_on_sale", "Put product on sale"),)

    def __str__(self):
        return self.name
