from rest_framework import serializers
from .models import Business
from user.models import User


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        
        fields = ('id','name', 'description' )

class BusinessRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ('name', 'description', 'citiz_front_image', 'citiz_back_image', 'optional_docs1_image', 'optional_docs2_image', 'optional_docs3_image', 'user')



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email', 'phone_no', 'first_name', 'last_name', 'address', 'image', 'user_type', 'authority_role')

