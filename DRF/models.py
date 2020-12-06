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
    extra_name = models.CharField(
        max_length=250, editable=False, default="null")
    # created_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.name
    # or
    # def __str__(self):
    #     return f"{self.name} - {self.created_at.strftime(' %H: %M: %S')}"
    # or
    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ("-created_at",)  # showing in assending order
        verbose_name_plural = "Custom Test Model"

    # benifits of extra_name (editable= False)
    # this will overwrite (def __str__) method
    def save(self, *args, **kwargs):
        self.extra_name = f"{self.name} - {self.phone_number}"
        super().save(*args, **kwargs)


class ModelX(models.Model):
    # ForeignKey means we can add one model with same value multiple times
    test_content = models.ForeignKey(
        TestModel, on_delete=models.CASCADE, related_name='test_content')  # rename the inherited class
    mileage = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str__(self):
        return f"{self.test_content.name} - {self.mileage}"

    class Meta:
        ordering = ("-created_at",)  # showing in assending order
        verbose_name_plural = "Model X"


class ModelY(models.Model):
    # OneTwoOneField means there will be single relations with the inherited class.we can not add a same value multiple times.
    test_content = models.OneToOneField(
        TestModel, on_delete=models.CASCADE, related_name='test_content_y')  # rename the inherited class
    mileage = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str__(self):
        return f"{self.test_content.name} - {self.mileage}"

    class Meta:
        ordering = ("-created_at",)  # showing in assending order
        verbose_name_plural = "Model Y"
