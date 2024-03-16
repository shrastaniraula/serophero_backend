from rest_framework import serializers
from .models import Business


class BusinessUserSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    user_name = serializers.CharField()
    user_image = serializers.CharField()
    user_type = serializers.CharField()
    business_name = serializers.CharField()

