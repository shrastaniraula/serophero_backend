from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        
        fields = ('receiver','sender', 'message', 'created' )

class MessageListSerializer(serializers.Serializer):
    user_email = serializers.CharField()
    user_fullname = serializers.CharField()
    user_image = serializers.CharField()
    user_id = serializers.CharField()
    my_id = serializers.CharField()
    latest_message = serializers.CharField()
    datetime = serializers.DateTimeField()
    sent_by_me = serializers.BooleanField()

