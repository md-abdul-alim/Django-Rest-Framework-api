from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.


class TestModel(models.Model):
    name = models.CharField(max_length=255, unique=True, null=True, blank=True)
    description = models.TextField()
    phone_number = models.PositiveIntegerField()
    is_live = BooleanField()
    amount = models.FloatField()
