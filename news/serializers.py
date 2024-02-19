from rest_framework import serializers

from user.models import User

from .models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields= ['id','author', 'news_heading', 'news_description', 'news_image', 'post_date', 'is_verified']


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id','username', 'email', 'phone_no', 'first_name', 'last_name', 'address', 'image', 'user_type', 'authority_role')



        