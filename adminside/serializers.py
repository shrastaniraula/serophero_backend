from rest_framework import serializers
from business.models import Business
from news.models import News
from user.models import User

class BusinessAdminSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    def get_user_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    
    class Meta:
        model = Business
        fields = ['id', 'name', 'citiz_front_image', 'citiz_back_image', 'optional_docs1_image',
                'optional_docs2_image', 'optional_docs3_image', 'description', 'is_verified',
                'user', 'user_name', 'created_at']



class NewsAdminSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    def get_user_name(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"
    
    class Meta:
        model = News
        fields = ['id', 'author', 'user_name', 'news_heading', 'news_description', 'news_image',
                'post_date', 'is_verified', 'report_count']
        

class UserAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
