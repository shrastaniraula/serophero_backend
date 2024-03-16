from rest_framework import serializers
from user.models import User
from .models import News


class NewsSerializer(serializers.Serializer):
    news_id = serializers.IntegerField()
    news_title = serializers.CharField()
    news_description = serializers.CharField()
    news_image = serializers.CharField()
    news_date = serializers.DateTimeField()
    user_name = serializers.CharField()
    user_id = serializers.CharField()




        