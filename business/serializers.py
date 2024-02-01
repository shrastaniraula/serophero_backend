from rest_framework import serializers
from .models import Business
from user.models import User


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        
        fields = ('id','name', 'description')



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email', 'phone_no', 'first_name', 'last_name', 'address', 'image')

