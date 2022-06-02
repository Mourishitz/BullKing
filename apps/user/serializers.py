from .models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(required=True)
    birthday = serializers.DateField(required=True)
    is_active = serializers.BooleanField(required=False, default=True)
    diet = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = [
            'id',
            'gender',
            'email',
            'birthday',
            'last_name',
            'first_name',
            'is_active',
            'diet',
        ]
