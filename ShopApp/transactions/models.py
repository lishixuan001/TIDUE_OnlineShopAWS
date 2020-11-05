from django.db import models
from django.utils.timezone import now


class Person(models.Model):
    name = models.CharField(default=None, null=True, blank=True, max_length=100)
    time = models.DateTimeField(default=now, editable=False)
    image = models.ImageField(upload_to='images/')