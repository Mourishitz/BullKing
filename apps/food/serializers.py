from .models import Food
from rest_framework import serializers


class FoodSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(required=True)
    carbs = serializers.FloatField(required=False, default=0)
    fiber = serializers.FloatField(required=False, default=0)
    sugar = serializers.FloatField(required=False, default=0)
    sodium = serializers.FloatField(required=False, default=0)
    protein = serializers.FloatField(required=False, default=0)
    calories = serializers.FloatField(required=False, default=0)
    total_fat = serializers.FloatField(required=False, default=0)
    trans_fat = serializers.FloatField(required=False, default=0)
    saturated_fat = serializers.FloatField(required=False, default=0)


    class Meta:
        model = Food
        fields = [
            'id',
            'name',
            'carbs',
            'fiber',
            'sugar',
            'sodium',
            'protein',
            'calories',
            'total_fat',
            'trans_fat',
            'saturated_fat',
        ]
