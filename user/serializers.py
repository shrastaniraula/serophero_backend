from rest_framework import serializers

from business.serializers import BusinessUserSerializer
from events.serializers import EventSerializer
from .models import User

        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email', 'phone_no', 'first_name', 'last_name', 'address', 'image', 'user_type', 'authority_role')



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'phone_no', 'password', 'first_name', 'last_name', 'address')

class UserDetailsSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    user_fullname = serializers.CharField()
    user_name = serializers.CharField()
    user_location = serializers.CharField()
    user_contact = serializers.CharField()
    user_email = serializers.CharField()
    user_image = serializers.CharField()
    user_type = serializers.CharField()
    authority_role = serializers.CharField()
    business_name = serializers.CharField()
    business_description = serializers.CharField()


class CombinedHomeSerializer(serializers.Serializer):
    user_details = UserDetailsSerializer()
    business_details = BusinessUserSerializer(many=True)
    event_details = EventSerializer(many=True) 

