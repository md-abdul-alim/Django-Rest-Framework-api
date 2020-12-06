from django.db import models
from django.db.models.fields import BooleanField
from django.utils import timezone
# Create your models here.


class TestModel(models.Model):
    name = models.CharField(max_length=255, unique=True, null=True, blank=True)
    description = models.TextField()
    phone_number = models.PositiveIntegerField()
    is_live = BooleanField()
    amount = models.FloatField()
    # created_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.name
    def __str__(self):
        return f"{self.name} - {self.created_at.strftime(' %H: %M: %S')}"

    class Meta:
        ordering = ("created_at",)  # showing in assending order
