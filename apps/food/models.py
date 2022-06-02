from django.db import models
from apps.core.models import Core


class Food(Core):
    name = models.CharField(max_length=150, unique=True)
    carbs = models.FloatField(blank=True, null=True, default=0)
    fiber = models.FloatField(blank=True, null=True, default=0)
    sugar = models.FloatField(blank=True, null=True, default=0)
    sodium = models.FloatField(blank=True, null=True, default=0)
    protein = models.FloatField(blank=True, null=True, default=0)
    calories = models.FloatField(blank=True, null=True, default=0)
    total_fat = models.FloatField(blank=True, null=True, default=0)
    trans_fat = models.FloatField(blank=True, null=True, default=0)
    saturated_fat = models.FloatField(blank=True, null=True, default=0)
