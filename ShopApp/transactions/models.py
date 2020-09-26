from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils import timezone


class Product(models.Model):
    def __str__(self):
        return "{name}".format(name=self.name)

    def update(self):
        self.sufficient = self.stock > self.limit

    limit = models.IntegerField(default=5)

    name = models.CharField(default=None, null=True, blank=True, max_length=100)
    idx = models.CharField(default=None, null=True, blank=True, max_length=100)
    price = models.FloatField(default=None, null=True, blank=True)
    stock = models.IntegerField(default=None, null=True, blank=True)
    sufficient = models.BooleanField(default=True)
