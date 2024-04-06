from rest_framework import serializers
from .models import Message, Suggestions


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


class SuggestionsSerializer(serializers.ModelSerializer):
    sender_name = serializers.SerializerMethodField()
    sender_image = serializers.SerializerMethodField()


    def get_sender_name(self, obj):
        return f"{obj.by.first_name} {obj.by.last_name}"
    
    def get_sender_image(self, obj):
        return f"{obj.by.image}"
    
    class Meta:
        model = Suggestions
        fields= ('by', 'description', 'datetime' , 'sender_name','sender_image')


