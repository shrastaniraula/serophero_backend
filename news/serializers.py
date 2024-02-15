from rest_framework import serializers

from .models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields= ['author', 'news_heading', 'news_description', 'news_image', 'post_date', 'is_verified']

        